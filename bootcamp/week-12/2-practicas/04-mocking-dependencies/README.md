# 🎭 Práctica 04: Mocking Dependencies

## 🎯 Objetivo

Aprender a usar mocking para aislar componentes y testear código con dependencias externas.

---

## 📋 Descripción

En esta práctica aprenderás a:

- Usar unittest.mock (Mock, MagicMock, patch)
- Mockear servicios externos (email, APIs)
- Usar pytest-mock para simplificar mocking
- Mockear tiempo y datetime
- Verificar llamadas a mocks

---

## 📁 Estructura

```
04-mocking-dependencies/
├── README.md
├── pyproject.toml
├── src/
│   ├── __init__.py
│   ├── services.py        # Servicios con dependencias
│   ├── notifications.py   # Servicio de notificaciones
│   └── external_api.py    # Cliente de API externa
└── tests/
    ├── __init__.py
    ├── conftest.py
    ├── test_mocking.py    # Tests con mocks
    └── test_patching.py   # Tests con patch
```

---

## 🚀 Instrucciones

### Paso 1: Configurar el proyecto

```bash
cd 04-mocking-dependencies
uv sync
```

### Paso 2: Explorar los servicios

Revisa los archivos en `src/` para entender las dependencias.

### Paso 3: Escribir tests con mocks

Descomenta los tests y completa las secciones.

### Paso 4: Ejecutar tests

```bash
uv run pytest -v -s
```

---

## ✅ Criterios de Éxito

- [ ] Mocks configurados correctamente
- [ ] Verificación de llamadas a mocks
- [ ] Uso de patch para servicios externos
- [ ] Tests de servicios con dependencias

---

## ⏱️ Tiempo Estimado

30 minutos
