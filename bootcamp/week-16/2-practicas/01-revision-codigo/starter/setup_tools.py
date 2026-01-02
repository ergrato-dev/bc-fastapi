"""
============================================
PRÁCTICA 01: Revisión de Código
Archivo: setup_tools.py
============================================

Este archivo configura las herramientas de análisis estático
para tu proyecto FastAPI.

Herramientas que configuraremos:
1. Ruff - Linter ultra rápido
2. Pyright - Type checker
3. Bandit - Análisis de seguridad
"""

# ============================================
# PASO 1: Archivo pyproject.toml
# ============================================
print("--- Paso 1: Configuración en pyproject.toml ---")

# Agrega esta configuración a tu pyproject.toml:
PYPROJECT_CONFIG = """
# ============================================
# RUFF - Linter y Formatter
# ============================================
[tool.ruff]
target-version = "py312"
line-length = 88
fix = true

[tool.ruff.lint]
select = [
    "E",      # pycodestyle errors
    "W",      # pycodestyle warnings
    "F",      # Pyflakes
    "I",      # isort
    "B",      # flake8-bugbear
    "C4",     # flake8-comprehensions
    "UP",     # pyupgrade
    "ARG",    # flake8-unused-arguments
    "SIM",    # flake8-simplify
    "TCH",    # flake8-type-checking
    "PTH",    # flake8-use-pathlib
    "ERA",    # eradicate (commented code)
    "PL",     # Pylint
    "RUF",    # Ruff-specific rules
]
ignore = [
    "E501",   # line too long (handled by formatter)
    "PLR0913", # too many arguments
]

[tool.ruff.lint.per-file-ignores]
"tests/*" = ["ARG", "PLR2004"]  # Allow magic values in tests
"alembic/*" = ["ERA"]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"

# ============================================
# PYRIGHT - Type Checker
# ============================================
[tool.pyright]
pythonVersion = "3.12"
typeCheckingMode = "basic"
reportMissingImports = true
reportMissingTypeStubs = false
reportUnusedVariable = true
reportUnusedImport = true

# ============================================
# BANDIT - Security Analysis
# ============================================
[tool.bandit]
exclude_dirs = ["tests", "alembic"]
skips = ["B101"]  # Skip assert warnings in tests

# ============================================
# PYTEST - Testing
# ============================================
[tool.pytest.ini_options]
testpaths = ["tests"]
asyncio_mode = "auto"
addopts = "-v --tb=short"

[tool.coverage.run]
source = ["src"]
omit = ["*/tests/*", "*/alembic/*"]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "if TYPE_CHECKING:",
    "raise NotImplementedError",
]
"""

print(PYPROJECT_CONFIG)
print("\n✅ Copia esta configuración a tu pyproject.toml")


# ============================================
# PASO 2: Instalar dependencias de desarrollo
# ============================================
print("\n--- Paso 2: Instalar herramientas ---")

INSTALL_COMMANDS = """
# Agregar herramientas de desarrollo con uv
uv add --dev ruff pyright bandit pytest pytest-asyncio pytest-cov

# O si usas pip
pip install ruff pyright bandit pytest pytest-asyncio pytest-cov
"""

print(INSTALL_COMMANDS)


# ============================================
# PASO 3: Scripts útiles
# ============================================
print("\n--- Paso 3: Scripts en pyproject.toml ---")

SCRIPTS_CONFIG = """
# Agregar a pyproject.toml para crear comandos útiles
[project.scripts]
lint = "ruff check src tests"
format = "ruff format src tests"
typecheck = "pyright src"
security = "bandit -r src"
test = "pytest"
test-cov = "pytest --cov=src --cov-report=html"
"""

print(SCRIPTS_CONFIG)


# ============================================
# PASO 4: Pre-commit hooks (opcional pero recomendado)
# ============================================
print("\n--- Paso 4: Pre-commit hooks ---")

PRECOMMIT_CONFIG = """
# Crear archivo .pre-commit-config.yaml en la raíz del proyecto
# Esto ejecuta checks automáticamente antes de cada commit

repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.8.0
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format

  - repo: https://github.com/RobertCraiworthy/pyright-python
    rev: v1.1.390
    hooks:
      - id: pyright

  - repo: https://github.com/PyCQA/bandit
    rev: 1.7.10
    hooks:
      - id: bandit
        args: ["-c", "pyproject.toml"]
        additional_dependencies: ["bandit[toml]"]

# Instalar pre-commit:
# uv add --dev pre-commit
# pre-commit install
"""

print(PRECOMMIT_CONFIG)


# ============================================
# PASO 5: Verificar instalación
# ============================================
print("\n--- Paso 5: Verificar instalación ---")

VERIFY_COMMANDS = """
# Verificar que las herramientas están instaladas
ruff --version
pyright --version
bandit --version

# Si todo está correcto, verás las versiones instaladas
"""

print(VERIFY_COMMANDS)

print("\n" + "="*50)
print("✅ Configuración completa!")
print("Continúa con run_analysis.sh para ejecutar el análisis")
print("="*50)
