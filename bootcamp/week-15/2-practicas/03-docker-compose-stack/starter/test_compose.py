"""
Tests para Docker Compose Stack - Práctica 03
"""

import subprocess
import sys
import time
import urllib.request
import json


def run_command(cmd: list[str], timeout: int = 120) -> tuple[int, str]:
    """Ejecutar comando."""
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return result.returncode, result.stdout + result.stderr
    except Exception as e:
        return 1, str(e)


def test_compose_up():
    """Test que docker compose levanta todos los servicios."""
    print("🚀 Starting docker compose stack...")
    
    # Detener si hay algo corriendo
    run_command(["docker", "compose", "down", "-v"])
    
    # Levantar
    code, output = run_command(["docker", "compose", "up", "-d", "--build"], timeout=180)
    
    if code != 0:
        print(f"❌ Failed to start stack:\n{output}")
        return False
    
    # Esperar a que los servicios estén listos
    print("   Waiting for services to be ready...")
    time.sleep(10)
    
    print("✅ Docker compose stack started")
    return True


def test_services_running():
    """Test que todos los servicios están corriendo."""
    print("🔍 Checking running services...")
    
    code, output = run_command(["docker", "compose", "ps", "--format", "json"])
    
    try:
        services = []
        for line in output.strip().split('\n'):
            if line:
                services.append(json.loads(line))
        
        expected = ["api", "db", "redis"]
        running = [s.get("Service") for s in services if s.get("State") == "running"]
        
        for service in expected:
            if service in running:
                print(f"   ✅ {service} is running")
            else:
                print(f"   ❌ {service} is NOT running")
                return False
        
        return True
    except Exception as e:
        print(f"⚠️ Could not parse services: {e}")
        # Fallback: check manually
        code, output = run_command(["docker", "compose", "ps"])
        print(output)
        return "Up" in output


def test_api_health():
    """Test API health endpoint."""
    print("🏥 Testing API health...")
    
    max_attempts = 10
    for attempt in range(max_attempts):
        try:
            req = urllib.request.Request("http://localhost:8000/health")
            with urllib.request.urlopen(req, timeout=5) as response:
                if response.status == 200:
                    print("✅ API health check passed")
                    return True
        except Exception:
            if attempt < max_attempts - 1:
                print(f"   Attempt {attempt + 1}/{max_attempts}...")
                time.sleep(3)
    
    print("❌ API health check failed")
    return False


def test_db_connection():
    """Test PostgreSQL connection through API."""
    print("🐘 Testing PostgreSQL connection...")
    
    try:
        req = urllib.request.Request("http://localhost:8000/db-check")
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read())
            
            if data.get("status") == "connected":
                print(f"✅ PostgreSQL connected (version: {data.get('version', 'unknown')[:20]}...)")
                return True
            else:
                print(f"❌ PostgreSQL error: {data.get('error', 'unknown')}")
                return False
    except Exception as e:
        print(f"❌ Could not check DB: {e}")
        return False


def test_redis_connection():
    """Test Redis connection through API."""
    print("📦 Testing Redis connection...")
    
    try:
        req = urllib.request.Request("http://localhost:8000/redis-check")
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read())
            
            if data.get("status") == "connected":
                print(f"✅ Redis connected (version: {data.get('version', 'unknown')})")
                return True
            else:
                print(f"❌ Redis error: {data.get('error', 'unknown')}")
                return False
    except Exception as e:
        print(f"❌ Could not check Redis: {e}")
        return False


def test_cache_operations():
    """Test Redis cache set/get through API."""
    print("💾 Testing cache operations...")
    
    try:
        # Set value
        data = "test-value-123".encode()
        req = urllib.request.Request(
            "http://localhost:8000/cache/test-key?value=test-value-123",
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=5) as response:
            result = json.loads(response.read())
            if result.get("status") != "ok":
                print(f"❌ Cache set failed: {result}")
                return False
        
        # Get value
        req = urllib.request.Request("http://localhost:8000/cache/test-key")
        with urllib.request.urlopen(req, timeout=5) as response:
            result = json.loads(response.read())
            if result.get("value") == "test-value-123":
                print("✅ Cache operations work correctly")
                return True
            else:
                print(f"❌ Cache get returned wrong value: {result}")
                return False
    except Exception as e:
        print(f"❌ Cache operations failed: {e}")
        return False


def cleanup():
    """Limpiar recursos."""
    print("\n🧹 Cleaning up...")
    run_command(["docker", "compose", "down", "-v"])
    print("✅ Cleanup complete")


def main():
    print("=" * 50)
    print("🐳 Docker Compose Stack Tests - Práctica 03")
    print("=" * 50)
    print()
    
    tests = [
        test_compose_up,
        test_services_running,
        test_api_health,
        test_db_connection,
        test_redis_connection,
        test_cache_operations,
    ]
    
    results = []
    for test in tests:
        try:
            results.append(test())
        except Exception as e:
            print(f"❌ Test error: {e}")
            results.append(False)
        print()
    
    cleanup()
    
    print("\n" + "=" * 50)
    passed = sum(results)
    total = len(results)
    
    if passed == total:
        print(f"🎉 All {total} tests passed!")
    else:
        print(f"⚠️ {passed}/{total} tests passed")
    
    sys.exit(0 if passed == total else 1)


if __name__ == "__main__":
    main()
