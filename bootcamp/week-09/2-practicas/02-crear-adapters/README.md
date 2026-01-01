# 🔧 Práctica 02: Crear Adapters

## 🎯 Objetivo

Implementar **Adapters** concretos que satisfagan los Protocols definidos en la práctica anterior.

---

## 📋 Descripción

Crearás adapters para el sistema de notificaciones:

- `EmailAdapter` - Envío de emails (simulado)
- `SMSAdapter` - Envío de SMS (simulado)
- `ConsoleAdapter` - Imprime en consola (desarrollo)
- `InMemoryNotificationRepository` - Persistencia en memoria

---

## ⏱️ Duración

45 minutos

---

## 📁 Estructura

```
02-crear-adapters/
├── README.md
└── starter/
    ├── pyproject.toml
    └── src/
        ├── __init__.py
        ├── domain/
        │   ├── __init__.py
        │   ├── entities/
        │   │   └── notification.py
        │   └── ports/
        │       ├── notification_sender.py
        │       └── notification_repository.py
        └── infrastructure/
            ├── __init__.py
            └── adapters/
                ├── __init__.py
                ├── email_adapter.py
                ├── sms_adapter.py
                ├── console_adapter.py
                └── in_memory_repository.py
```

---

## 🚀 Instrucciones

### Paso 1: Crear EmailAdapter

Abre `starter/src/infrastructure/adapters/email_adapter.py` y descomenta el código.

### Paso 2: Crear SMSAdapter

Abre `starter/src/infrastructure/adapters/sms_adapter.py` y descomenta el código.

### Paso 3: Crear ConsoleAdapter

Abre `starter/src/infrastructure/adapters/console_adapter.py` y descomenta el código.

### Paso 4: Crear InMemoryNotificationRepository

Abre `starter/src/infrastructure/adapters/in_memory_repository.py` y descomenta el código.

### Paso 5: Ejecutar el script de prueba

```bash
cd starter
uv run python -m src.main
```

---

## ✅ Criterios de Éxito

- [ ] Los adapters implementan todos los métodos del Protocol
- [ ] NO heredan del Protocol (duck typing)
- [ ] Tienen configuración inyectada en constructor
- [ ] El código pasa el type checker
