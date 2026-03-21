# 💉 Práctica 03: Inyección de Dependencias Avanzada

## 🎯 Objetivo

Implementar **inyección de dependencias** usando FastAPI `Depends()` para conectar servicios con adapters de forma desacoplada.

---

## 📋 Descripción

Aprenderás a:

- Crear factories que retornan adapters según configuración
- Usar `Depends()` para inyectar dependencias
- Cambiar implementaciones sin modificar servicios
- Configurar diferentes adapters por entorno

---

## ⏱️ Duración

40 minutos

---

## 📁 Estructura

```
03-inyeccion-dependencias/
├── README.md
└── starter/
    ├── pyproject.toml
    └── src/
        ├── main.py
        ├── config.py
        ├── domain/
        │   ├── entities/
        │   └── ports/
        ├── application/
        │   └── services/
        │       └── notification_service.py
        ├── infrastructure/
        │   └── adapters/
        └── presentation/
            ├── dependencies.py
            └── routers/
                └── notifications.py
```

---

## 🚀 Instrucciones

### Paso 1: Configurar settings por entorno

Abre `starter/src/config.py` y revisa la configuración.

### Paso 2: Crear el NotificationService

Abre `starter/src/application/services/notification_service.py` y descomenta.

### Paso 3: Implementar factories en dependencies.py

Abre `starter/src/presentation/dependencies.py` y descomenta las factories.

### Paso 4: Crear el router con inyección

Abre `starter/src/presentation/routers/notifications.py` y descomenta.

### Paso 5: Probar la API

```bash
cd starter
uv run fastapi dev src/main.py
```

---

## ✅ Criterios de Éxito

- [ ] El service recibe ports, no adapters concretos
- [ ] Las factories crean adapters según configuración
- [ ] Cambiar `ENV=test` usa fake adapters
- [ ] La API funciona correctamente
