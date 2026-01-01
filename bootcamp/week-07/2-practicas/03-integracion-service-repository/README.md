# 🔨 Práctica 03: Integración Service-Repository

## 🎯 Objetivo

Conectar Services con Repositories de forma correcta, manteniendo la separación de responsabilidades.

---

## 📋 Contexto

El Service debe recibir los Repositories por inyección de dependencias, no crearlos internamente.

---

## 📝 Instrucciones

### Paso 1: Revisar modelos y repositorios

Los archivos `models.py` y `repositories.py` ya están completos.

### Paso 2: Implementar OrderService

En `starter/services.py`, descomenta el `OrderService` que usa repositorios.

### Paso 3: Configurar dependencias FastAPI

En `starter/main.py`, descomenta las funciones de dependencias y endpoints.

### Paso 4: Probar

```bash
cd starter
uv run fastapi dev main.py
```

Prueba crear usuarios, productos y órdenes en `/docs`.

---

## ✅ Resultado Esperado

- Service NO conoce SQLAlchemy
- Repositories son inyectados via `Depends()`
- Lógica de negocio (validaciones) en Service
- Acceso a datos en Repository
