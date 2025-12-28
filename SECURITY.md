# 🔒 Política de Seguridad

## Versiones Soportadas

| Versión | Soportada |
| ------- | --------- |
| main    | ✅        |

## Reportar una Vulnerabilidad

La seguridad de este proyecto es importante para nosotros. Si descubres una vulnerabilidad de seguridad, te pedimos que la reportes de manera responsable.

### ⚠️ NO hacer público el reporte

Por favor, **NO** abras un issue público para reportar vulnerabilidades de seguridad.

### 📧 Cómo Reportar

1. **Abre un Security Advisory privado** en GitHub:
   - Ve a la pestaña "Security" del repositorio
   - Haz clic en "Report a vulnerability"
   - Completa el formulario con los detalles

2. **Incluye en tu reporte**:
   - Descripción detallada de la vulnerabilidad
   - Pasos para reproducir el problema
   - Impacto potencial
   - Sugerencias de solución (si las tienes)

### ⏱️ Tiempo de Respuesta

- **Confirmación inicial**: 48 horas
- **Evaluación**: 7 días
- **Resolución**: Dependiendo de la severidad

### 🎁 Reconocimiento

Agradecemos a todos los investigadores de seguridad que reportan vulnerabilidades de manera responsable. Tu nombre será incluido en nuestros agradecimientos (si lo deseas).

## Mejores Prácticas de Seguridad

Este bootcamp enseña las siguientes prácticas de seguridad:

### Validación de Datos

```python
# ✅ Usar Pydantic para validación
from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)
```

### Autenticación

```python
# ✅ Usar hashing seguro para contraseñas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
```

### Variables de Entorno

```python
# ✅ Nunca hardcodear secretos
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    secret_key: str
    database_url: str
    
    class Config:
        env_file = ".env"
```

### SQL Injection

```python
# ✅ Usar ORM (SQLAlchemy) - evita SQL injection
user = db.query(User).filter(User.email == email).first()

# ❌ NUNCA hacer esto
# db.execute(f"SELECT * FROM users WHERE email = '{email}'")
```

## Dependencias

Mantenemos las dependencias actualizadas para evitar vulnerabilidades conocidas. Usamos:

- `uv` para gestión de dependencias
- Dependabot para alertas automáticas
- Auditorías regulares de seguridad

---

Gracias por ayudar a mantener este proyecto seguro. 🛡️
