# 🚦 Práctica 01: Rate Limiting con slowapi

## 🎯 Objetivos

- Instalar y configurar slowapi en FastAPI
- Aplicar límites a endpoints específicos
- Manejar respuestas 429 correctamente
- Implementar límites dinámicos por tipo de usuario

---

## 📋 Descripción

En esta práctica implementaremos rate limiting para proteger una API de usuarios contra abusos. Configuraremos diferentes límites para endpoints públicos, autenticados y administrativos.

---

## ⏱️ Duración

**35 minutos**

---

## 📁 Estructura

```
01-rate-limiting-slowapi/
├── README.md
└── starter/
    ├── pyproject.toml
    ├── main.py
    └── test_rate_limit.py
```

---

## 🚀 Pasos

### Paso 1: Configuración Inicial

Primero, revisemos la estructura del proyecto y las dependencias necesarias.

**Abre `starter/pyproject.toml`** para ver las dependencias:

```toml
[project]
dependencies = [
    "fastapi>=0.115.0",
    "uvicorn[standard]>=0.32.0",
    "slowapi>=0.1.9",
]
```

Instala las dependencias:

```bash
cd starter
uv sync
```

---

### Paso 2: Configurar el Limiter

**Abre `starter/main.py`** y descomenta la sección del Paso 2.

El limiter necesita:
1. Una función `key_func` para identificar clientes
2. Registro en el estado de la app
3. Handler para errores de rate limit

```python
# La función key_func determina cómo identificar a cada cliente
# get_remote_address usa la IP del cliente
```

---

### Paso 3: Aplicar Límites a Endpoints

Descomenta la sección del Paso 3 en `main.py`.

Observa cómo se aplican diferentes límites:
- `/public` - 20 requests por minuto (acceso libre)
- `/auth/login` - 5 por minuto (proteger contra brute force)
- `/api/users` - 30 por minuto (endpoints de API)

```python
# El decorador @limiter.limit() va ANTES del decorador de ruta
# Formato: "N/periodo" donde periodo puede ser second, minute, hour, day
```

---

### Paso 4: Límites Dinámicos

Descomenta la sección del Paso 4.

Los límites dinámicos permiten diferentes cuotas según el usuario:
- Usuarios premium: 100/minuto
- Usuarios normales: 30/minuto
- No autenticados: 10/minuto

```python
# La función dinámica recibe el Request y retorna un string de límite
```

---

### Paso 5: Excluir Endpoints

Descomenta la sección del Paso 5.

Algunos endpoints no deberían tener límite:
- Health checks
- Métricas de Prometheus
- Documentación

```python
# El decorador @limiter.exempt excluye el endpoint del rate limiting
```

---

### Paso 6: Handler Personalizado

Descomenta la sección del Paso 6.

Personaliza la respuesta 429 para incluir información útil:
- Tiempo de espera
- Límite alcanzado
- Mensaje amigable

---

### Paso 7: Ejecutar y Probar

1. Inicia el servidor:
```bash
uv run uvicorn main:app --reload
```

2. Prueba el endpoint público:
```bash
# Ejecutar muchas veces rápidamente
for i in {1..25}; do curl -s http://localhost:8000/public | jq .; done
```

3. Verifica la respuesta 429:
```bash
# Después de exceder el límite
curl -i http://localhost:8000/public
```

4. Ejecuta los tests:
```bash
uv run pytest test_rate_limit.py -v
```

---

## ✅ Verificación

Tu implementación está correcta si:

- [ ] El endpoint `/public` bloquea después de 20 requests/minuto
- [ ] El endpoint `/auth/login` bloquea después de 5 requests/minuto
- [ ] Los headers `X-RateLimit-*` aparecen en las respuestas
- [ ] La respuesta 429 incluye `Retry-After`
- [ ] El endpoint `/health` no tiene límite
- [ ] Los tests pasan

---

## 🔍 Headers de Respuesta Esperados

```http
HTTP/1.1 200 OK
X-RateLimit-Limit: 20
X-RateLimit-Remaining: 19
X-RateLimit-Reset: 1705312345

# Después de exceder:
HTTP/1.1 429 Too Many Requests
Retry-After: 45
X-RateLimit-Limit: 20
X-RateLimit-Remaining: 0
```

---

## 🎯 Retos Adicionales

1. **Redis Backend**: Configura slowapi para usar Redis
2. **Límites por Endpoint**: Diferentes límites por método HTTP
3. **Whitelist**: Excluir ciertas IPs del rate limiting

---

## 📚 Recursos

- [slowapi Documentation](https://slowapi.readthedocs.io/)
- [Rate Limiting Best Practices](https://cloud.google.com/architecture/rate-limiting-strategies)
