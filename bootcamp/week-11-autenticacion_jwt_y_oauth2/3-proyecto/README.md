# 🔐 Proyecto Semana 11: API con Autenticación JWT y RBAC

## 🏛️ Tu Dominio Asignado

**Dominio**: `[El instructor te asignará tu dominio único]`

> ⚠️ **IMPORTANTE**: Cada aprendiz trabaja sobre un dominio diferente.

### 💡 Ejemplo Genérico de Referencia

> Los ejemplos usan **"Warehouse"** (Almacén) que NO está en el pool.
> **Debes adaptar TODO a tu dominio asignado.**

| Concepto | Ejemplo Genérico | Adapta a tu Dominio |
|----------|-----------------|---------------------|
| Protected Resource | `Item` | `{YourEntity}` |
| Roles | `admin, warehouse_manager, operator` | `admin, {role1}, {role2}` |
| Permissions | `items:read, items:write` | `{entities}:read, {entities}:write` |

---

## 🎯 Objetivo

Implementar **Autenticación y Autorización completa**:

- JWT con refresh tokens
- RBAC (Role-Based Access Control)
- Permisos granulares
- Protección de endpoints

---

## 📦 Requisitos Funcionales (Adapta a tu Dominio)

### User Model con Roles

```python
# Ejemplo genérico (Warehouse)
from enum import Enum
from sqlalchemy.orm import Mapped, mapped_column

class Role(str, Enum):
    ADMIN = "admin"
    WAREHOUSE_MANAGER = "warehouse_manager"
    OPERATOR = "operator"
    VIEWER = "viewer"

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]
    role: Mapped[Role] = mapped_column(default=Role.VIEWER)
    is_active: Mapped[bool] = mapped_column(default=True)

# Permisos por rol
ROLE_PERMISSIONS = {
    Role.ADMIN: ["items:*", "zones:*", "users:*"],
    Role.WAREHOUSE_MANAGER: ["items:read", "items:write", "zones:read"],
    Role.OPERATOR: ["items:read", "items:write"],
    Role.VIEWER: ["items:read", "zones:read"],
}
```

### JWT Service

```python
# Ejemplo genérico
from datetime import datetime, timedelta
from jose import jwt, JWTError

class JWTService:
    def __init__(self, settings: Settings):
        self.secret = settings.JWT_SECRET
        self.algorithm = settings.JWT_ALGORITHM
        self.access_expire = settings.ACCESS_TOKEN_EXPIRE_MINUTES
        self.refresh_expire = settings.REFRESH_TOKEN_EXPIRE_DAYS
    
    def create_access_token(self, user_id: int, role: str) -> str:
        expire = datetime.utcnow() + timedelta(minutes=self.access_expire)
        payload = {
            "sub": str(user_id),
            "role": role,
            "type": "access",
            "exp": expire
        }
        return jwt.encode(payload, self.secret, algorithm=self.algorithm)
    
    def create_refresh_token(self, user_id: int) -> str:
        expire = datetime.utcnow() + timedelta(days=self.refresh_expire)
        payload = {
            "sub": str(user_id),
            "type": "refresh",
            "exp": expire
        }
        return jwt.encode(payload, self.secret, algorithm=self.algorithm)
    
    def decode_token(self, token: str) -> dict | None:
        try:
            return jwt.decode(token, self.secret, algorithms=[self.algorithm])
        except JWTError:
            return None
```

### Permission Dependencies

```python
# Ejemplo genérico
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    jwt_service: JWTService = Depends(get_jwt_service),
    user_repo: IUserRepository = Depends(get_user_repo)
) -> User:
    payload = jwt_service.decode_token(token)
    if not payload or payload.get("type") != "access":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )
    
    user = await user_repo.find_by_id(int(payload["sub"]))
    if not user or not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found or inactive"
        )
    return user

def require_permission(permission: str):
    """Factory para verificar permisos"""
    async def permission_checker(
        user: User = Depends(get_current_user)
    ) -> User:
        user_permissions = ROLE_PERMISSIONS.get(user.role, [])
        
        # Verificar permiso exacto o wildcard
        has_permission = (
            permission in user_permissions or
            f"{permission.split(':')[0]}:*" in user_permissions
        )
        
        if not has_permission:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Permission '{permission}' required"
            )
        return user
    
    return permission_checker
```

### Protected Endpoints

```python
# Ejemplo genérico
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/")
async def list_items(
    user: User = Depends(require_permission("items:read")),
    item_service: ItemService = Depends(get_item_service)
):
    """Listar items - requiere items:read"""
    return await item_service.list_all()

@router.post("/")
async def create_item(
    data: ItemCreate,
    user: User = Depends(require_permission("items:write")),
    item_service: ItemService = Depends(get_item_service)
):
    """Crear item - requiere items:write"""
    return await item_service.create(data, created_by=user.id)

@router.delete("/{item_id}")
async def delete_item(
    item_id: int,
    user: User = Depends(require_permission("items:*")),
    item_service: ItemService = Depends(get_item_service)
):
    """Eliminar item - requiere items:* (solo admin/manager)"""
    return await item_service.delete(item_id)
```

### Auth Endpoints

```python
# Ejemplo genérico
@router.post("/auth/login")
async def login(
    form: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthService = Depends(get_auth_service)
):
    tokens = await auth_service.login(form.username, form.password)
    return {
        "access_token": tokens.access_token,
        "refresh_token": tokens.refresh_token,
        "token_type": "bearer"
    }

@router.post("/auth/refresh")
async def refresh_token(
    refresh_token: str,
    auth_service: AuthService = Depends(get_auth_service)
):
    new_tokens = await auth_service.refresh(refresh_token)
    return new_tokens
```

---

## 🗂️ Estructura del Proyecto

```
starter/
├── main.py
├── auth/
│   ├── __init__.py
│   ├── jwt_service.py
│   ├── password_service.py
│   ├── dependencies.py
│   └── router.py
├── models/
│   └── user.py
├── permissions/
│   ├── roles.py
│   └── checker.py
├── routers/
│   └── items.py  # Endpoints protegidos
├── pyproject.toml
├── Dockerfile
└── docker-compose.yml
```

---

## ✅ Criterios de Evaluación

| Criterio | Puntos |
|----------|--------|
| **Funcionalidad** (40%) | |
| JWT funciona correctamente | 15 |
| RBAC implementado | 15 |
| Refresh token funciona | 10 |
| **Adaptación al Dominio** (35%) | |
| Roles relevantes al negocio | 12 |
| Permisos específicos | 13 |
| Originalidad (no copia ejemplo) | 10 |
| **Calidad del Código** (25%) | |
| Seguridad adecuada | 10 |
| Dependencies bien estructuradas | 10 |
| Código limpio | 5 |
| **Total** | **100** |

---

## ⚠️ Política Anticopia

- ❌ **No copies** los roles "warehouse_manager/operator"
- ✅ **Diseña** roles específicos de tu dominio
- ✅ **Crea** permisos relevantes para tu negocio

---

## 📚 Recursos

- [FastAPI Security](https://fastapi.tiangolo.com/tutorial/security/)
- [python-jose JWT](https://python-jose.readthedocs.io/)
- [Pool de Dominios](../../../_apprentices-only/dominios/POOL-DOMINIOS.md)

---

**Tiempo estimado:** 3 horas

[← Volver a Prácticas](../2-practicas/) | [Recursos →](../4-recursos/)
