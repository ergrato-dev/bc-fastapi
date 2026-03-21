# 🔐 Práctica 02: Security Headers y CORS

## 🎯 Objetivos

- Configurar CORS correctamente en FastAPI
- Implementar security headers con middleware
- Prevenir ataques comunes (XSS, Clickjacking)
- Manejar errores de forma segura

---

## 📋 Descripción

En esta práctica implementaremos múltiples capas de seguridad para proteger una API. Configuraremos CORS para controlar accesos desde otros dominios y añadiremos headers de seguridad recomendados por OWASP.

---

## ⏱️ Duración

**30 minutos**

---

## 📁 Estructura

```
02-security-headers/
├── README.md
└── starter/
    ├── pyproject.toml
    ├── main.py
    ├── middleware.py
    └── test_security.py
```

---

## 🚀 Pasos

### Paso 1: Configuración de CORS

**Abre `starter/main.py`** y descomenta la sección del Paso 1.

CORS (Cross-Origin Resource Sharing) controla qué dominios pueden acceder a tu API:

```python
# ❌ Nunca usar en producción:
# allow_origins=["*"]

# ✅ Especificar dominios permitidos:
# allow_origins=["https://mi-frontend.com"]
```

---

### Paso 2: Security Headers Middleware

**Abre `starter/middleware.py`** y descomenta la sección del Paso 2.

Implementa un middleware que añada headers de seguridad a cada respuesta:

- `X-Content-Type-Options: nosniff`
- `X-Frame-Options: DENY`
- `X-XSS-Protection: 1; mode=block`
- `Referrer-Policy: strict-origin-when-cross-origin`

---

### Paso 3: Content Security Policy (CSP)

Descomenta la sección del Paso 3 en `middleware.py`.

CSP controla qué recursos puede cargar el navegador:

```
Content-Security-Policy: default-src 'self'; script-src 'self'
```

---

### Paso 4: HSTS (HTTP Strict Transport Security)

Descomenta la sección del Paso 4.

HSTS fuerza el uso de HTTPS:

```
Strict-Transport-Security: max-age=31536000; includeSubDomains
```

---

### Paso 5: Manejo Seguro de Errores

Descomenta la sección del Paso 5 en `main.py`.

Los errores no deben exponer información interna:

```python
# ❌ MAL
{"error": str(exception), "traceback": "..."}

# ✅ BIEN
{"error": "internal_error", "message": "Something went wrong"}
```

---

### Paso 6: Ejecutar y Probar

1. Inicia el servidor:
```bash
cd starter
uv sync
uv run uvicorn main:app --reload
```

2. Verifica los security headers:
```bash
curl -I http://localhost:8000/api/data
```

3. Prueba CORS:
```bash
# Request con Origin
curl -H "Origin: https://allowed-domain.com" \
     -I http://localhost:8000/api/data
```

4. Ejecuta los tests:
```bash
uv run pytest test_security.py -v
```

---

## ✅ Verificación

Tu implementación está correcta si:

- [ ] CORS solo permite orígenes específicos
- [ ] El header `X-Content-Type-Options` está presente
- [ ] El header `X-Frame-Options` está presente
- [ ] Los errores no exponen stack traces
- [ ] Los tests pasan

---

## 🔍 Headers de Respuesta Esperados

```http
HTTP/1.1 200 OK
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-XSS-Protection: 1; mode=block
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: geolocation=(), microphone=()
Access-Control-Allow-Origin: https://allowed-domain.com
```

---

## 📚 Recursos

- [OWASP Secure Headers](https://owasp.org/www-project-secure-headers/)
- [MDN CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
- [Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP)
