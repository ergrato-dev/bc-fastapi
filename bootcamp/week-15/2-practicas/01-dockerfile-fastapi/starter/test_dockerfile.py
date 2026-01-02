"""
Tests para verificar el Dockerfile - Práctica 01
Ejecutar: python test_dockerfile.py
"""

import subprocess
import sys
import time
import urllib.request
import urllib.error


def run_command(cmd: list[str], capture: bool = True) -> tuple[int, str]:
    """Ejecutar comando y retornar código de salida y output."""
    try:
        result = subprocess.run(
            cmd,
            capture_output=capture,
            text=True,
            timeout=120,
        )
        return result.returncode, result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        return 1, "Command timed out"
    except Exception as e:
        return 1, str(e)


def test_image_builds():
    """Test que la imagen se construye correctamente."""
    print("🔨 Building Docker image...")
    code, output = run_command([
        "docker", "build", "-t", "fastapi-basic-test", "."
    ])
    
    if code != 0:
        print(f"❌ Build failed:\n{output}")
        return False
    
    print("✅ Image builds successfully")
    return True


def test_image_size():
    """Test que la imagen tiene un tamaño razonable."""
    print("📏 Checking image size...")
    code, output = run_command([
        "docker", "images", "fastapi-basic-test", "--format", "{{.Size}}"
    ])
    
    if code != 0:
        print(f"❌ Could not get image size")
        return False
    
    size_str = output.strip()
    print(f"   Image size: {size_str}")
    
    # Convertir a MB aproximado
    if "GB" in size_str:
        print("❌ Image is too large (> 1GB)")
        return False
    elif "MB" in size_str:
        size_mb = float(size_str.replace("MB", "").strip())
        if size_mb > 300:
            print(f"⚠️ Image is larger than recommended ({size_mb}MB > 300MB)")
        else:
            print(f"✅ Image size is good ({size_mb}MB)")
        return True
    
    print("✅ Image size is acceptable")
    return True


def test_container_starts():
    """Test que el contenedor inicia correctamente."""
    print("🚀 Starting container...")
    
    # Limpiar contenedor previo si existe
    run_command(["docker", "rm", "-f", "fastapi-test-container"])
    
    # Iniciar contenedor
    code, output = run_command([
        "docker", "run", "-d",
        "--name", "fastapi-test-container",
        "-p", "18000:8000",
        "fastapi-basic-test"
    ])
    
    if code != 0:
        print(f"❌ Container failed to start:\n{output}")
        return False
    
    # Esperar a que inicie
    time.sleep(3)
    
    # Verificar que está corriendo
    code, output = run_command([
        "docker", "ps", "-q", "-f", "name=fastapi-test-container"
    ])
    
    if not output.strip():
        # Ver logs si no está corriendo
        _, logs = run_command(["docker", "logs", "fastapi-test-container"])
        print(f"❌ Container is not running. Logs:\n{logs}")
        return False
    
    print("✅ Container starts successfully")
    return True


def test_health_endpoint():
    """Test que el health endpoint responde."""
    print("🏥 Testing health endpoint...")
    
    max_attempts = 5
    for attempt in range(max_attempts):
        try:
            req = urllib.request.Request("http://localhost:18000/health")
            with urllib.request.urlopen(req, timeout=5) as response:
                if response.status == 200:
                    print("✅ Health endpoint responds with 200")
                    return True
        except urllib.error.URLError:
            if attempt < max_attempts - 1:
                print(f"   Attempt {attempt + 1}/{max_attempts} failed, retrying...")
                time.sleep(2)
            continue
        except Exception as e:
            print(f"   Error: {e}")
            if attempt < max_attempts - 1:
                time.sleep(2)
            continue
    
    print("❌ Health endpoint not responding")
    return False


def test_info_endpoint():
    """Test que el info endpoint muestra variables de entorno."""
    print("ℹ️ Testing info endpoint...")
    
    try:
        req = urllib.request.Request("http://localhost:18000/info")
        with urllib.request.urlopen(req, timeout=5) as response:
            import json
            data = json.loads(response.read())
            
            env = data.get("environment", {})
            if env.get("PYTHONDONTWRITEBYTECODE") == "1":
                print("✅ PYTHONDONTWRITEBYTECODE is set")
            else:
                print("⚠️ PYTHONDONTWRITEBYTECODE not set (optional)")
            
            if env.get("PYTHONUNBUFFERED") == "1":
                print("✅ PYTHONUNBUFFERED is set")
            else:
                print("⚠️ PYTHONUNBUFFERED not set (optional)")
            
            return True
    except Exception as e:
        print(f"❌ Info endpoint error: {e}")
        return False


def cleanup():
    """Limpiar recursos de test."""
    print("\n🧹 Cleaning up...")
    run_command(["docker", "rm", "-f", "fastapi-test-container"])
    run_command(["docker", "rmi", "fastapi-basic-test"])
    print("✅ Cleanup complete")


def main():
    """Ejecutar todos los tests."""
    print("=" * 50)
    print("🐳 Dockerfile Tests - Práctica 01")
    print("=" * 50)
    print()
    
    tests = [
        test_image_builds,
        test_image_size,
        test_container_starts,
        test_health_endpoint,
        test_info_endpoint,
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"❌ Test error: {e}")
            results.append(False)
        print()
    
    cleanup()
    
    # Resumen
    print("\n" + "=" * 50)
    print("📊 Results Summary")
    print("=" * 50)
    
    passed = sum(results)
    total = len(results)
    
    if passed == total:
        print(f"🎉 All {total} tests passed!")
        sys.exit(0)
    else:
        print(f"⚠️ {passed}/{total} tests passed")
        sys.exit(1)


if __name__ == "__main__":
    main()
