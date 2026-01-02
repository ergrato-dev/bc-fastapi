# 🔐 Proyecto Semana 11: Sistema de Autenticación JWT

## 📋 Descripción

Construirás un **sistema de autenticación completo** para una API REST usando FastAPI, JWT y OAuth2. El sistema permitirá registro de usuarios, login, tokens de acceso/refresh, y endpoints protegidos con autorización basada en roles.

---

## 🎯 Objetivos de Aprendizaje

Al completar este proyecto demostrarás:

- ✅ Implementar OAuth2 Password Flow con FastAPI
- ✅ Crear y validar tokens JWT (access y refresh)
- ✅ Hashear passwords de forma segura con bcrypt
- ✅ Proteger endpoints con dependencias de autenticación
- ✅ Implementar autorización basada en roles (RBAC)
- ✅ Manejar errores de autenticación correctamente

---

## 🏗️ Arquitectura del Proyecto

```
starter/
├── pyproject.toml
├── src/
│   ├── __init__.py
│   ├── main.py              # App FastAPI
│   ├── config.py            # Configuración (SECRET_KEY, etc.)
│   ├── database.py          # Conexión SQLite
│   │
│   ├── auth/                # Módulo de autenticación
│   │   ├── __init__.py
│   │   ├── router.py        # Endpoints: /register, /login, /refresh
│   │   ├── schemas.py       # UserCreate, UserResponse, Token
│   │   ├── security.py      # JWT y password hashing
│   │   └── dependencies.py  # get_current_user, require_role
│   │
│   └── users/               # Módulo de usuarios
│       ├── __init__.py
│       ├── router.py        # Endpoints: /users/me, /admin/*
│       ├── models.py        # Modelo SQLAlchemy User
│       └── crud.py          # Operaciones de base de datos
│
└── tests/
    ├── conftest.py          # Fixtures de pytest
    ├── test_auth.py         # Tests de autenticación
    └── test_users.py        # Tests de usuarios
```

---

## 📝 Requisitos Funcionales

### RF1: Registro de Usuarios

- `POST /auth/register`
- Recibe: email, password, full_name
- Valida que el email no exista
- Hashea el password con bcrypt
- Crea usuario con rol "user" por defecto
- Retorna usuario creado (sin password)

### RF2: Login (OAuth2 Token)

- `POST /auth/token`
- Recibe: username (email), password como form-data
- Valida credenciales
- Genera access_token (15 min) y refresh_token (7 días)
- Retorna tokens según especificación OAuth2

### RF3: Refresh Token

- `POST /auth/refresh`
- Recibe: refresh_token en body
- Valida que sea un refresh token válido
- Genera nuevos access_token y refresh_token
- Retorna nuevos tokens

### RF4: Perfil de Usuario

- `GET /users/me`
- Requiere autenticación (token válido)
- Retorna datos del usuario autenticado

### RF5: Actualizar Perfil

- `PATCH /users/me`
- Requiere autenticación
- Permite actualizar full_name
- Retorna usuario actualizado

### RF6: Panel de Admin

- `GET /admin/users`
- Requiere rol "admin"
- Lista todos los usuarios

### RF7: Promover Usuario

- `PATCH /admin/users/{user_id}/role`
- Requiere rol "admin"
- Cambia rol de un usuario

---

## 🔧 Instrucciones de Desarrollo

### Paso 1: Configurar Entorno

```bash
cd starter
uv sync
```

### Paso 2: Revisar Estructura

Familiarízate con la estructura del proyecto y los archivos que debes completar.

### Paso 3: Completar TODOs

Busca los comentarios `# TODO:` en los archivos y completa la implementación:

1. **src/auth/security.py** - Funciones de JWT y password
2. **src/auth/dependencies.py** - Dependencias de autenticación
3. **src/auth/router.py** - Endpoints de auth
4. **src/users/crud.py** - Operaciones CRUD
5. **src/users/router.py** - Endpoints protegidos

### Paso 4: Ejecutar la App

```bash
uv run fastapi dev src/main.py
```

### Paso 5: Probar en Swagger

1. Ir a http://localhost:8000/docs
2. Registrar un usuario en `/auth/register`
3. Hacer login en `/auth/token`
4. Click en **Authorize** y pegar el token
5. Probar endpoints protegidos

### Paso 6: Ejecutar Tests

```bash
uv run pytest tests/ -v
```

---

## ✅ Criterios de Evaluación

### Funcionalidad (40%)

| Criterio | Puntos |
|----------|--------|
| Registro funcional | 10 |
| Login retorna tokens válidos | 10 |
| Refresh token funcional | 10 |
| Endpoints protegidos correctamente | 10 |

### Seguridad (30%)

| Criterio | Puntos |
|----------|--------|
| Passwords hasheados con bcrypt | 10 |
| JWT con claims correctos (sub, exp, type) | 10 |
| RBAC implementado correctamente | 10 |

### Código (20%)

| Criterio | Puntos |
|----------|--------|
| Type hints en funciones | 5 |
| Manejo de errores apropiado | 10 |
| Código limpio y organizado | 5 |

### Tests (10%)

| Criterio | Puntos |
|----------|--------|
| Tests pasan correctamente | 10 |

---

## 📚 Recursos de Apoyo

- [FastAPI Security](https://fastapi.tiangolo.com/tutorial/security/)
- [OAuth2 with Password](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)
- [python-jose Documentation](https://python-jose.readthedocs.io/)
- Teoría de la semana en `1-teoria/`

---

## 🎁 Bonus (Opcional)

- [ ] Implementar logout con blacklist de tokens
- [ ] Añadir validación de fortaleza de password
- [ ] Implementar rate limiting en login
- [ ] Añadir endpoint para cambiar password

---

## 📤 Entregables

1. Código fuente completado en `starter/`
2. Todos los tests pasando
3. Documentación de la API accesible en `/docs`
