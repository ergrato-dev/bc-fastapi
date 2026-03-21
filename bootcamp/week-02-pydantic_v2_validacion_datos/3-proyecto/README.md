# 📦 Proyecto Semana 02: API CRUD con Validación Pydantic

## 🏛️ Tu Dominio Asignado

**Dominio**: `[El instructor te asignará tu dominio único]`

> ⚠️ **IMPORTANTE**: Cada aprendiz trabaja sobre un dominio diferente.

### 💡 Ejemplo Genérico de Referencia

> Los ejemplos usan **"Warehouse"** (Almacén) que NO está en el pool.
> **Debes adaptar TODO a tu dominio asignado.**

| Concepto | Ejemplo Genérico | Adapta a tu Dominio |
|----------|-----------------|---------------------|
| Main Entity | `Item` | `{YourEntity}` |
| CRUD Endpoints | `/items/` | `/{your_entities}/` |
| Unique Field | `sku` | `{your_unique_field}` |

---

## 🎯 Objetivo

Construir una **API REST CRUD completa** para gestionar la entidad principal de tu dominio usando Pydantic v2 para validación de datos.

---

## 📦 Requisitos Funcionales (Adapta a tu Dominio)

### Entity Model (Mínimo 8 campos)

```python
# Ejemplo genérico (Warehouse - Item)
Item:
    id: int               # Auto-generated
    sku: str              # Unique, 3-20 chars, uppercase
    name: str             # 2-100 chars
    description: str | None
    category: CategoryEnum
    quantity: int         # >= 0
    unit_price: Decimal   # > 0, 2 decimals
    location: str         # Warehouse location (A-01, B-12, etc.)
    is_active: bool       # Default: True
    created_at: datetime
    updated_at: datetime | None
```

### Validadores Específicos

```python
# Ejemplo genérico
@field_validator("sku")
def validate_sku(cls, v: str) -> str:
    # Formato: 3 letras + guión + 3-5 números
    if not re.match(r"^[A-Z]{3}-\d{3,5}$", v):
        raise ValueError("SKU must be format: ABC-12345")
    return v

@field_validator("location")
def validate_location(cls, v: str) -> str:
    # Formato: Letra + guión + 2 dígitos
    if not re.match(r"^[A-Z]-\d{2}$", v):
        raise ValueError("Location must be format: A-01")
    return v
```

### Endpoints CRUD

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/{entities}/` | Crear entidad (validar unicidad) |
| GET | `/{entities}/` | Listar con paginación (skip, limit) |
| GET | `/{entities}/{id}` | Obtener por ID |
| GET | `/{entities}/by-{unique}/{value}` | Buscar por campo único |
| PATCH | `/{entities}/{id}` | Actualización parcial |
| DELETE | `/{entities}/{id}` | Eliminar |

**Ejemplo genérico (Warehouse):**
```bash
POST /items/
GET /items/?skip=0&limit=10&category=electronics
GET /items/42
GET /items/by-sku/ABC-12345
PATCH /items/42
DELETE /items/42
```

---

## 🗂️ Estructura del Proyecto

```
starter/
├── main.py
├── models.py          # Pydantic schemas
├── validators.py      # Custom validators
├── database.py        # In-memory storage
├── pyproject.toml
├── Dockerfile
└── docker-compose.yml
```

---

## ✅ Criterios de Evaluación

| Criterio | Puntos |
|----------|--------|
| **Funcionalidad** (40%) | |
| CRUD completo funciona | 15 |
| Validaciones Pydantic correctas | 15 |
| Paginación y filtros | 10 |
| **Adaptación al Dominio** (35%) | |
| Campos coherentes con negocio | 12 |
| Validadores específicos | 13 |
| Originalidad (no copia ejemplo) | 10 |
| **Calidad del Código** (25%) | |
| Schemas bien estructurados | 10 |
| Type hints correctos | 10 |
| Código limpio | 5 |
| **Total** | **100** |

---

## ⚠️ Política Anticopia

- ❌ **No copies** el ejemplo genérico "Warehouse/Item"
- ✅ **Diseña** campos específicos de tu dominio
- ✅ **Crea** validadores únicos para tu negocio

---

## 📚 Recursos

- [Pydantic v2 Docs](https://docs.pydantic.dev/)
- [FastAPI Request Body](https://fastapi.tiangolo.com/tutorial/body/)
- [Pool de Dominios](../../../_apprentices-only/dominios/POOL-DOMINIOS.md)

---

**Tiempo estimado:** 2-3 horas

[← Volver a Prácticas](../2-practicas/) | [Recursos →](../4-recursos/)
