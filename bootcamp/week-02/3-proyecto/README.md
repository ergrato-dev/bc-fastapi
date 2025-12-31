# 📦 Proyecto Semana 02: API de Gestión de Contactos

## 🎯 Objetivo

Construir una API REST completa para gestionar contactos usando Pydantic v2 para validación de datos.

---

## 📋 Descripción

Crearás una API que permita:

- Crear contactos con validación estricta
- Listar contactos con paginación
- Buscar contactos por email
- Actualizar contactos parcialmente
- Eliminar contactos

---

## 🛠️ Requisitos Técnicos

### Modelo de Contacto

```python
Contact:
    id: int (autogenerado)
    first_name: str (2-50 caracteres)
    last_name: str (2-50 caracteres)
    email: EmailStr (único)
    phone: str (formato: +52 XXX XXX XXXX)
    company: str | None
    tags: list[str] (máximo 5 tags)
    is_favorite: bool (default: False)
    created_at: datetime
    updated_at: datetime | None
```

### Schemas Requeridos

1. **ContactBase**: Campos comunes
2. **ContactCreate**: Para POST (sin id, timestamps)
3. **ContactUpdate**: Para PATCH (todos opcionales)
4. **ContactResponse**: Para respuestas (con id, timestamps)
5. **ContactList**: Lista paginada con total

### Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| POST | `/contacts` | Crear contacto |
| GET | `/contacts` | Listar con paginación |
| GET | `/contacts/{id}` | Obtener por ID |
| GET | `/contacts/email/{email}` | Buscar por email |
| PATCH | `/contacts/{id}` | Actualizar parcialmente |
| DELETE | `/contacts/{id}` | Eliminar |
| POST | `/contacts/{id}/favorite` | Marcar como favorito |

---

## ✅ Criterios de Aceptación

### Validaciones Obligatorias

- [ ] Email debe ser único (error 409 si ya existe)
- [ ] Teléfono debe normalizarse al formato `+52 XXX XXX XXXX`
- [ ] Tags deben estar en minúsculas sin duplicados
- [ ] Nombres deben capitalizarse automáticamente

### Validadores Requeridos

- [ ] `@field_validator` para normalizar teléfono
- [ ] `@field_validator` para capitalizar nombres
- [ ] `@field_validator` para procesar tags
- [ ] `@model_validator` para validar que email no cambie a uno existente

### Response Models

- [ ] Usar `response_model` en todos los endpoints
- [ ] No exponer datos internos innecesarios
- [ ] Usar status codes apropiados (201, 204, 404, 409, 422)

---

## 📁 Estructura del Proyecto

```
starter/
├── main.py           # Aplicación FastAPI y endpoints
├── schemas.py        # Modelos Pydantic (TODO)
├── database.py       # Simulación de base de datos
├── pyproject.toml
├── Dockerfile
└── docker-compose.yml
```

---

## 🚀 Cómo Empezar

### 1. Levantar el proyecto

```bash
cd starter
docker compose up --build
```

### 2. Acceder a la documentación

Visita http://localhost:8000/docs

### 3. Implementar schemas.py

Abre `schemas.py` y completa los TODOs:

1. Crear `ContactBase` con campos comunes
2. Crear `ContactCreate` con validadores
3. Crear `ContactUpdate` con campos opcionales
4. Crear `ContactResponse` con from_attributes
5. Crear `ContactList` para paginación

### 4. Probar los endpoints

Usa Swagger UI o curl para probar cada endpoint.

---

## 🧪 Casos de Prueba

### Crear Contacto Válido

```bash
curl -X POST http://localhost:8000/contacts \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "  alice  ",
    "last_name": "  garcía  ",
    "email": "alice@example.com",
    "phone": "5551234567",
    "tags": ["Work", "VIP", "work"]
  }'
```

**Respuesta esperada:**
```json
{
  "id": 1,
  "first_name": "Alice",
  "last_name": "García",
  "email": "alice@example.com",
  "phone": "+52 555 123 4567",
  "company": null,
  "tags": ["work", "vip"],
  "is_favorite": false,
  "created_at": "2025-12-31T10:00:00",
  "updated_at": null
}
```

### Crear con Email Duplicado

```bash
curl -X POST http://localhost:8000/contacts \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "Bob",
    "last_name": "Smith",
    "email": "alice@example.com",
    "phone": "5559876543"
  }'
```

**Respuesta esperada:** `409 Conflict`

### Update Parcial

```bash
curl -X PATCH http://localhost:8000/contacts/1 \
  -H "Content-Type: application/json" \
  -d '{"company": "TechCorp"}'
```

---

## 📊 Rúbrica de Evaluación

| Criterio | Puntos |
|----------|--------|
| Schemas correctamente definidos | 25 |
| Validadores implementados | 25 |
| Endpoints funcionando | 20 |
| Response models aplicados | 15 |
| Manejo de errores | 15 |
| **Total** | **100** |

---

## 💡 Hints

1. **Normalizar teléfono**: Usa regex para extraer solo dígitos, luego formatea
2. **Tags únicos**: Usa `set()` para eliminar duplicados, luego convierte a lista
3. **Email único**: Revisa en la "base de datos" antes de crear/actualizar
4. **exclude_unset**: Usa `model_dump(exclude_unset=True)` para PATCH

---

## 🔗 Recursos

- [Pydantic Validators](https://docs.pydantic.dev/latest/concepts/validators/)
- [FastAPI Response Model](https://fastapi.tiangolo.com/tutorial/response-model/)
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

---

[← Volver a Prácticas](../2-practicas/) | [Recursos →](../4-recursos/)
