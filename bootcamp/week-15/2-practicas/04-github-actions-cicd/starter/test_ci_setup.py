# ============================================
# Test Script - Verificar configuración CI/CD
# Semana 15 - Práctica 04
# ============================================
#
# Ejecuta este script para verificar que tu
# configuración de CI/CD está correcta.
#
# Uso: python test_ci_setup.py
# ============================================

import os
import subprocess
import sys
from pathlib import Path


def print_header(message: str) -> None:
    """Print a formatted header"""
    print(f"\n{'='*50}")
    print(f"  {message}")
    print(f"{'='*50}")


def print_result(success: bool, message: str) -> None:
    """Print a test result"""
    status = "✅" if success else "❌"
    print(f"{status} {message}")


def check_workflow_file() -> bool:
    """Verify workflow file exists and has correct structure"""
    print_header("Verificando archivo de workflow")

    workflow_path = Path(".github/workflows/ci.yml")

    if not workflow_path.exists():
        print_result(False, "Archivo .github/workflows/ci.yml no encontrado")
        return False

    print_result(True, "Archivo ci.yml encontrado")

    # Read and check content
    content = workflow_path.read_text()

    checks = [
        ("name:" in content, "Workflow tiene nombre definido"),
        ("on:" in content, "Triggers configurados (on:)"),
        ("jobs:" in content, "Jobs definidos"),
        ("runs-on:" in content, "Runner configurado (runs-on)"),
        ("actions/checkout" in content, "Usando actions/checkout"),
        ("actions/setup-python" in content, "Usando actions/setup-python"),
    ]

    all_passed = True
    for condition, message in checks:
        # Check if line is not commented
        lines = content.split("\n")
        uncommented = any(
            condition.split(":")[0] in line and not line.strip().startswith("#")
            for line in lines
            if ":" in condition
        )

        if "actions/" in condition:
            uncommented = any(
                condition in line and not line.strip().startswith("#")
                for line in lines
            )

        print_result(uncommented, message)
        if not uncommented:
            all_passed = False

    return all_passed


def check_project_structure() -> bool:
    """Verify project has correct structure for CI"""
    print_header("Verificando estructura del proyecto")

    required_files = [
        ("requirements.txt", "Archivo requirements.txt"),
        ("Dockerfile", "Dockerfile"),
        ("src/main.py", "Código fuente src/main.py"),
        ("tests/test_api.py", "Tests tests/test_api.py"),
    ]

    all_exist = True
    for filepath, description in required_files:
        exists = Path(filepath).exists()
        print_result(exists, description)
        if not exists:
            all_exist = False

    return all_exist


def check_dockerfile() -> bool:
    """Verify Dockerfile has production best practices"""
    print_header("Verificando Dockerfile")

    dockerfile = Path("Dockerfile")
    if not dockerfile.exists():
        print_result(False, "Dockerfile no encontrado")
        return False

    content = dockerfile.read_text()

    checks = [
        ("FROM python:3.13" in content or "FROM python:3.12" in content, "Usando Python 3.12+"),
        ("AS builder" in content or "AS runtime" in content, "Multi-stage build"),
        ("HEALTHCHECK" in content, "Health check configurado"),
        ("USER" in content and "root" not in content.split("USER")[-1][:20], "Usuario no-root"),
    ]

    all_passed = True
    for condition, message in checks:
        print_result(condition, message)
        if not condition:
            all_passed = False

    return all_passed


def run_lint_check() -> bool:
    """Try to run ruff check"""
    print_header("Ejecutando lint (ruff)")

    try:
        result = subprocess.run(
            ["ruff", "check", "src/"],
            capture_output=True,
            text=True,
        )
        success = result.returncode == 0
        print_result(success, "ruff check pasó" if success else f"ruff check falló: {result.stdout}")
        return success
    except FileNotFoundError:
        print_result(False, "ruff no está instalado (pip install ruff)")
        return False


def run_tests() -> bool:
    """Try to run pytest"""
    print_header("Ejecutando tests (pytest)")

    try:
        result = subprocess.run(
            ["pytest", "-v", "--tb=short"],
            capture_output=True,
            text=True,
        )
        success = result.returncode == 0

        if success:
            # Count passed tests
            lines = result.stdout.split("\n")
            for line in lines:
                if "passed" in line:
                    print_result(True, line.strip())
                    break
        else:
            print_result(False, "Algunos tests fallaron")
            print(result.stdout)

        return success
    except FileNotFoundError:
        print_result(False, "pytest no está instalado (pip install pytest)")
        return False


def build_docker_image() -> bool:
    """Try to build Docker image"""
    print_header("Construyendo imagen Docker")

    try:
        result = subprocess.run(
            ["docker", "build", "-t", "cicd-test:latest", "."],
            capture_output=True,
            text=True,
        )
        success = result.returncode == 0
        print_result(success, "Imagen construida exitosamente" if success else "Error construyendo imagen")

        if not success:
            print(result.stderr[:500])  # Show first 500 chars of error

        return success
    except FileNotFoundError:
        print_result(False, "Docker no está instalado o no está en PATH")
        return False


def main() -> None:
    """Run all checks"""
    print("\n" + "=" * 50)
    print("  🔄 Verificación de CI/CD Setup")
    print("=" * 50)

    results = {
        "Estructura del proyecto": check_project_structure(),
        "Archivo de workflow": check_workflow_file(),
        "Dockerfile": check_dockerfile(),
    }

    # Optional checks (require tools installed)
    print("\n" + "-" * 50)
    print("  Checks opcionales (requieren herramientas)")
    print("-" * 50)

    if os.environ.get("RUN_FULL_CHECKS", "false").lower() == "true":
        results["Lint (ruff)"] = run_lint_check()
        results["Tests (pytest)"] = run_tests()
        results["Docker build"] = build_docker_image()
    else:
        print("\n💡 Para ejecutar checks completos:")
        print("   RUN_FULL_CHECKS=true python test_ci_setup.py")

    # Summary
    print_header("Resumen")

    passed = sum(1 for r in results.values() if r)
    total = len(results)

    for name, result in results.items():
        print_result(result, name)

    print(f"\n📊 Resultado: {passed}/{total} checks pasaron")

    if passed == total:
        print("\n🎉 ¡Tu configuración de CI/CD está lista!")
        print("   Haz push a GitHub para ver el workflow en acción.")
    else:
        print("\n⚠️  Revisa los checks que fallaron antes de continuar.")

    sys.exit(0 if passed == total else 1)


if __name__ == "__main__":
    main()
