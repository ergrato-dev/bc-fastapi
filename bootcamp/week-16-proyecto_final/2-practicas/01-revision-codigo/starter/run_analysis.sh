#!/bin/bash
# ============================================
# PRÁCTICA 01: Revisión de Código
# Archivo: run_analysis.sh
# ============================================
# 
# Ejecuta este script desde la raíz de tu proyecto:
# chmod +x run_analysis.sh
# ./run_analysis.sh
#
# ============================================

echo "============================================"
echo "🔍 ANÁLISIS DE CÓDIGO - Tu Proyecto FastAPI"
echo "============================================"
echo ""

# ============================================
# 1. RUFF - Linting
# ============================================
echo "📋 1. Ejecutando Ruff (linting)..."
echo "-------------------------------------------"

# Descomenta la siguiente línea:
# ruff check src/ --output-format=grouped

echo ""
echo "💡 Para auto-fix de errores simples:"
# ruff check src/ --fix

echo ""

# ============================================
# 2. RUFF - Formatting
# ============================================
echo "🎨 2. Verificando formato con Ruff..."
echo "-------------------------------------------"

# Descomenta la siguiente línea:
# ruff format src/ --check

echo ""
echo "💡 Para formatear automáticamente:"
# ruff format src/

echo ""

# ============================================
# 3. PYRIGHT - Type Checking
# ============================================
echo "🔤 3. Ejecutando Pyright (type checking)..."
echo "-------------------------------------------"

# Descomenta la siguiente línea:
# pyright src/

echo ""

# ============================================
# 4. BANDIT - Security Analysis
# ============================================
echo "🔐 4. Ejecutando Bandit (seguridad)..."
echo "-------------------------------------------"

# Descomenta la siguiente línea:
# bandit -r src/ -f txt

echo ""
echo "💡 Para ver solo issues de alta severidad:"
# bandit -r src/ -ll

echo ""

# ============================================
# 5. TESTS con Coverage
# ============================================
echo "🧪 5. Ejecutando tests con coverage..."
echo "-------------------------------------------"

# Descomenta las siguientes líneas:
# pytest tests/ -v --cov=src --cov-report=term-missing

echo ""
echo "💡 Para generar reporte HTML:"
# pytest tests/ --cov=src --cov-report=html
# echo "Abre htmlcov/index.html en tu navegador"

echo ""

# ============================================
# 6. RESUMEN
# ============================================
echo "============================================"
echo "📊 RESUMEN DE ANÁLISIS"
echo "============================================"
echo ""
echo "Revisa los resultados de cada herramienta:"
echo ""
echo "✅ Ruff: Errores de estilo y bugs potenciales"
echo "✅ Pyright: Errores de tipos"
echo "✅ Bandit: Vulnerabilidades de seguridad"
echo "✅ Pytest: Tests y coverage"
echo ""
echo "Prioridad de corrección:"
echo "1. 🔴 Errores de seguridad (Bandit)"
echo "2. 🟠 Errores de tipos (Pyright)"
echo "3. 🟡 Bugs potenciales (Ruff)"
echo "4. 🟢 Estilo y formato (Ruff)"
echo ""
echo "============================================"

# ============================================
# COMANDOS ÚTILES ADICIONALES
# ============================================
# 
# Ver archivos con más problemas:
# ruff check src/ --statistics
#
# Ignorar regla específica en una línea:
# x = 1  # noqa: E501
#
# Ignorar regla en todo el archivo:
# # ruff: noqa: E501
#
# Ver qué reglas están activas:
# ruff rule --all
#
# ============================================
