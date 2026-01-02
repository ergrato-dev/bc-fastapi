# 🧪 Práctica 01: Primeros Tests con pytest

## 🎯 Objetivo

Aprender los fundamentos de pytest escribiendo tests básicos para funciones Python.

---

## 📋 Descripción

En esta práctica aprenderás a:

- Configurar pytest en un proyecto
- Escribir tests con assertions básicas
- Ejecutar tests desde la terminal
- Interpretar resultados de tests
- Usar markers y parametrización básica

---

## 📁 Estructura

```
01-primeros-tests/
├── README.md
├── pyproject.toml
├── src/
│   ├── __init__.py
│   └── calculator.py      # Funciones a testear
└── tests/
    ├── __init__.py
    └── test_calculator.py # Tests a descomentar
```

---

## 🚀 Instrucciones

### Paso 1: Configurar el proyecto

```bash
cd 01-primeros-tests
uv sync
```

### Paso 2: Explorar el código

Abre `src/calculator.py` y revisa las funciones implementadas.

### Paso 3: Escribir tests

Abre `tests/test_calculator.py` y descomenta cada sección de tests siguiendo las instrucciones.

### Paso 4: Ejecutar tests

```bash
# Ejecutar todos los tests
uv run pytest

# Con output detallado
uv run pytest -v

# Solo un test específico
uv run pytest tests/test_calculator.py::test_add_two_positive_numbers
```

---

## ✅ Criterios de Éxito

- [ ] Todos los tests pasan (`pytest` sin errores)
- [ ] Al menos 10 tests escritos
- [ ] Uso de `pytest.raises` para excepciones
- [ ] Al menos un test parametrizado

---

## ⏱️ Tiempo Estimado

30 minutos
