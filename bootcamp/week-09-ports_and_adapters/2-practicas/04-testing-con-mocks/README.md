# 🧪 Práctica 04: Testing con Fake Adapters

## 🎯 Objetivo

Aprender a testear servicios usando **fake adapters** en lugar de mocks, aplicando el patrón Spy para verificar interacciones.

---

## 📋 Descripción

Crearás tests para el NotificationService usando:

- Fake adapters en lugar de infraestructura real
- Patrón Spy para verificar llamadas
- Tests unitarios rápidos sin I/O

---

## ⏱️ Duración

45 minutos

---

## 📁 Estructura

```
04-testing-con-mocks/
├── README.md
└── starter/
    ├── pyproject.toml
    └── src/
        ├── domain/
        ├── application/
        └── tests/
            ├── __init__.py
            ├── conftest.py
            ├── fakes/
            │   ├── __init__.py
            │   ├── fake_repository.py
            │   └── fake_sender.py
            └── unit/
                ├── __init__.py
                └── test_notification_service.py
```

---

## 🚀 Instrucciones

### Paso 1: Crear FakeNotificationRepository

Abre `starter/src/tests/fakes/fake_repository.py` y descomenta.

### Paso 2: Crear SpyNotificationSender

Abre `starter/src/tests/fakes/fake_sender.py` y descomenta.

### Paso 3: Configurar fixtures en conftest.py

Abre `starter/src/tests/conftest.py` y descomenta.

### Paso 4: Implementar tests

Abre `starter/src/tests/unit/test_notification_service.py` y descomenta.

### Paso 5: Ejecutar tests

```bash
cd starter
uv run pytest -v
```

---

## ✅ Criterios de Éxito

- [ ] Tests ejecutan sin infraestructura real
- [ ] Fake repository persiste en memoria
- [ ] Spy sender registra llamadas
- [ ] Tests cubren happy path y error cases
