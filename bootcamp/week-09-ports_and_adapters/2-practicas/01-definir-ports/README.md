# 🔌 Práctica 01: Definir Ports con Protocols

## 🎯 Objetivo

Aprender a definir **Ports** (interfaces) usando `Protocol` de Python para establecer contratos claros entre el dominio y la infraestructura.

---

## 📋 Descripción

En esta práctica crearás los Ports para un **sistema de notificaciones**:

- `NotificationSender` - Para enviar notificaciones
- `NotificationRepository` - Para persistir notificaciones
- `TemplateRenderer` - Para renderizar plantillas

---

## ⏱️ Duración

40 minutos

---

## 📁 Estructura

```
01-definir-ports/
├── README.md
└── starter/
    ├── pyproject.toml
    └── src/
        ├── __init__.py
        └── domain/
            ├── __init__.py
            ├── entities/
            │   ├── __init__.py
            │   └── notification.py
            └── ports/
                ├── __init__.py
                ├── notification_sender.py
                ├── notification_repository.py
                └── template_renderer.py
```

---

## 🚀 Instrucciones

### Paso 1: Revisar la entidad de dominio

Abre `starter/src/domain/entities/notification.py` y familiarízate con la entidad `Notification`.

### Paso 2: Definir el Port NotificationSender

Abre `starter/src/domain/ports/notification_sender.py` y descomenta el código para definir el Protocol.

### Paso 3: Definir el Port NotificationRepository

Abre `starter/src/domain/ports/notification_repository.py` y descomenta el código.

### Paso 4: Definir el Port TemplateRenderer

Abre `starter/src/domain/ports/template_renderer.py` y descomenta el código.

### Paso 5: Verificar con type checker

Ejecuta el verificador de tipos para asegurar que los Protocols están bien definidos.

---

## ✅ Criterios de Éxito

- [ ] Todos los Protocols usan `typing.Protocol`
- [ ] Los métodos tienen type hints completos
- [ ] Cada Protocol tiene docstrings explicando el contrato
- [ ] El código pasa el type checker sin errores
