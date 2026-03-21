# 🔐 Práctica 04: Endpoints Protegidos

## 🎯 Objetivos

- Crear dependencia `get_current_user`
- Proteger endpoints con autenticación
- Implementar autorización basada en roles
- Extraer datos del usuario desde el token

---

## 📋 Instrucciones

En esta práctica implementarás endpoints que requieren autenticación.

### Paso 1: Revisar la Estructura

```
starter/
├── pyproject.toml
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── router.py
│   │   ├── security.py
│   │   ├── schemas.py
│   │   └── dependencies.py  # ← Completar get_current_user
│   └── users/
│       ├── __init__.py
│       ├── router.py        # ← Endpoints protegidos
│       └── fake_db.py
└── tests/
    └── test_protected.py
```

### Paso 2: Instalar Dependencias

```bash
cd starter
uv sync
```

### Paso 3: Implementar get_current_user

Abre `src/auth/dependencies.py` y completa la dependencia.

### Paso 4: Proteger Endpoints

Abre `src/users/router.py` y usa las dependencias.

### Paso 5: Probar en Swagger

1. Ir a http://localhost:8000/docs
2. Click en **Authorize** → Login con `user@example.com` / `password123`
3. Probar `/users/me` (debe retornar tus datos)
4. Probar `/admin/dashboard` (debe fallar con rol "user")

### Paso 6: Ejecutar Tests

```bash
uv run pytest tests/test_protected.py -v
```

---

## 🔑 Conceptos Clave

### Dependencia de Usuario

```python
# La dependencia extrae el usuario del token
async def get_current_user(
    token: str = Depends(oauth2_scheme)
) -> User:
    # 1. Decodificar token
    # 2. Extraer email del "sub"
    # 3. Buscar usuario en DB
    # 4. Retornar usuario o 401
```

### Proteger Endpoint

```python
@router.get("/me")
async def read_current_user(
    user: User = Depends(get_current_user)  # ← Requiere token
):
    return user
```

### Autorización por Rol

```python
def require_role(required_role: str):
    def checker(user: User = Depends(get_current_user)):
        if user.role != required_role:
            raise HTTPException(403, "Not authorized")
        return user
    return checker
```

---

## ✅ Criterios de Éxito

- [ ] `/users/me` retorna datos del usuario autenticado
- [ ] Endpoints sin token retornan 401
- [ ] Token inválido retorna 401
- [ ] Admin puede acceder a `/admin/dashboard`
- [ ] User NO puede acceder a `/admin/dashboard`
- [ ] Todos los tests pasan
