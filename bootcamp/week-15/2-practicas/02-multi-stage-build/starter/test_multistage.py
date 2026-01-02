"""
Tests para verificar Multi-Stage Build - Práctica 02
"""

import subprocess
import sys
import time
import urllib.request
import json


def run_command(cmd: list[str]) -> tuple[int, str]:
    """Ejecutar comando."""
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
        return result.returncode, result.stdout + result.stderr
    except Exception as e:
        return 1, str(e)


def test_image_builds():
    """Test que la imagen multi-stage se construye."""
    print("🔨 Building multi-stage image...")
    code, output = run_command(["docker", "build", "-t", "fastapi-multistage-test", "."])
    
    if code != 0:
        print(f"❌ Build failed:\n{output}")
        return False
    
    print("✅ Multi-stage image builds successfully")
    return True


def test_image_size():
    """Test que la imagen es pequeña."""
    print("📏 Checking image size...")
    code, output = run_command([
        "docker", "images", "fastapi-multistage-test", "--format", "{{.Size}}"
    ])
    
    size_str = output.strip()
    print(f"   Image size: {size_str}")
    
    if "MB" in size_str:
        size_mb = float(size_str.replace("MB", "").strip())
        if size_mb < 200:
            print(f"✅ Excellent! Image is under 200MB ({size_mb}MB)")
            return True
        elif size_mb < 300:
            print(f"⚠️ Good, but could be smaller ({size_mb}MB)")
            return True
        else:
            print(f"❌ Image is too large ({size_mb}MB > 300MB)")
            return False
    
    return True


def test_non_root_user():
    """Test que el contenedor corre como usuario no-root."""
    print("👤 Checking container user...")
    
    # Limpiar
    run_command(["docker", "rm", "-f", "multistage-test-container"])
    
    # Iniciar contenedor
    code, _ = run_command([
        "docker", "run", "-d",
        "--name", "multistage-test-container",
        "-p", "18001:8000",
        "fastapi-multistage-test"
    ])
    
    if code != 0:
        print("❌ Container failed to start")
        return False
    
    time.sleep(3)
    
    # Verificar usuario
    code, output = run_command([
        "docker", "exec", "multistage-test-container", "whoami"
    ])
    
    user = output.strip()
    print(f"   Container user: {user}")
    
    if user == "root":
        print("❌ Container is running as root!")
        return False
    elif user == "appuser":
        print("✅ Container runs as non-root user (appuser)")
        return True
    else:
        print(f"⚠️ Container runs as {user} (not root, but not appuser)")
        return True


def test_venv_in_path():
    """Test que el virtualenv está en el PATH."""
    print("🐍 Checking virtualenv in PATH...")
    
    try:
        time.sleep(2)
        req = urllib.request.Request("http://localhost:18001/info")
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read())
            
            venv_path = data.get("venv_path", "")
            if "/opt/venv" in venv_path or "/opt/venv" in str(data):
                print("✅ Virtualenv is properly configured")
                return True
            else:
                print("⚠️ Virtualenv path not detected in response")
                return True  # No es crítico
    except Exception as e:
        print(f"⚠️ Could not verify venv: {e}")
        return True


def test_health_endpoint():
    """Test health endpoint."""
    print("🏥 Testing health endpoint...")
    
    max_attempts = 5
    for attempt in range(max_attempts):
        try:
            req = urllib.request.Request("http://localhost:18001/health")
            with urllib.request.urlopen(req, timeout=5) as response:
                if response.status == 200:
                    print("✅ Health endpoint responds")
                    return True
        except Exception:
            if attempt < max_attempts - 1:
                time.sleep(2)
    
    print("❌ Health endpoint not responding")
    return False


def cleanup():
    """Limpiar recursos."""
    print("\n🧹 Cleaning up...")
    run_command(["docker", "rm", "-f", "multistage-test-container"])
    run_command(["docker", "rmi", "fastapi-multistage-test"])


def main():
    print("=" * 50)
    print("🐳 Multi-Stage Build Tests - Práctica 02")
    print("=" * 50)
    print()
    
    tests = [
        test_image_builds,
        test_image_size,
        test_non_root_user,
        test_venv_in_path,
        test_health_endpoint,
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
