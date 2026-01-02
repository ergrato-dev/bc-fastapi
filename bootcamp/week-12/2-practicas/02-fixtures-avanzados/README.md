# 🔩 Práctica 02: Fixtures Avanzados

## 🎯 Objetivo

Dominar el uso de fixtures en pytest: scope, yield, conftest.py y factories.

---

## 📋 Descripción

En esta práctica aprenderás a:

- Crear fixtures con setup y teardown
- Usar diferentes scopes (function, class, module, session)
- Compartir fixtures con conftest.py
- Crear fixture factories
- Usar fixtures parametrizadas

---

## 📁 Estructura

```
02-fixtures-avanzados/
├── README.md
├── pyproject.toml
├── src/
│   ├── __init__.py
│   └── models.py          # Modelos de datos
└── tests/
    ├── __init__.py
    ├── conftest.py        # Fixtures compartidas
    ├── test_fixtures.py   # Tests de fixtures básicas
    └── test_scopes.py     # Tests de scopes
```

---

## 🚀 Instrucciones

### Paso 1: Configurar el proyecto

```bash
cd 02-fixtures-avanzados
uv sync
```

### Paso 2: Estudiar conftest.py

Abre `tests/conftest.py` y revisa las fixtures definidas.

### Paso 3: Descomentar tests

Abre los archivos de test y descomenta cada sección.

### Paso 4: Ejecutar y observar

```bash
# Ejecutar con output para ver setup/teardown
uv run pytest -v -s

# Ver orden de ejecución de fixtures
uv run pytest --setup-show
```

---

## ✅ Criterios de Éxito

- [ ] Fixtures con yield funcionando
- [ ] Uso correcto de scopes
- [ ] conftest.py organizado
- [ ] Factory fixtures implementadas

---

## ⏱️ Tiempo Estimado

30 minutos
