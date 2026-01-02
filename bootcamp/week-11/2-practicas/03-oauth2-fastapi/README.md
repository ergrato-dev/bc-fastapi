# 🔄 Práctica 03: OAuth2 con FastAPI

## 🎯 Objetivos

- Implementar OAuth2 Password Flow
- Usar OAuth2PasswordBearer y OAuth2PasswordRequestForm
- Crear endpoint `/token` según especificación OAuth2
- Autenticar usuarios y generar tokens

---

## 📋 Instrucciones

En esta práctica implementarás el flujo completo de OAuth2 Password.

### Paso 1: Revisar la Estructura

```
starter/
├── pyproject.toml
├── src/
│   ├── __init__.py
│   ├── main.py           # App FastAPI
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── router.py     # ← Completar endpoint /token
│   │   ├── security.py   # Funciones JWT y password
│   │   └── schemas.py    # Schemas de respuesta
│   └── users/
│       ├── __init__.py
│       └── fake_db.py    # Base de datos simulada
└── tests/
    └── test_auth.py
```

### Paso 2: Instalar Dependencias

```bash
cd starter
uv sync
```

### Paso 3: Implementar OAuth2

Abre `src/auth/router.py` y completa el endpoint de token.

### Paso 4: Ejecutar la App

```bash
uv run fastapi dev src/main.py
```

### Paso 5: Probar en Swagger

1. Ir a http://localhost:8000/docs
2. Click en **Authorize**
3. Usar: `user@example.com` / `password123`
4. Probar endpoints protegidos

### Paso 6: Ejecutar Tests

```bash
uv run pytest tests/test_auth.py -v
```

---

## ✅ Criterios de Éxito

- [ ] `/auth/token` acepta form data (username, password)
- [ ] Retorna `access_token` y `token_type`
- [ ] Credenciales incorrectas retornan 401
- [ ] Swagger muestra el botón Authorize
- [ ] Todos los tests pasan
