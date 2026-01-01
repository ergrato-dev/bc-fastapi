# 📚 Proyecto: Library API

## 🎯 Objetivo

Construir una API REST completa para gestionar una biblioteca con libros y autores, aplicando todos los conceptos de SQLAlchemy ORM aprendidos esta semana.

**Duración estimada:** 2 horas

---

## 📋 Requerimientos

### Funcionalidades

1. **Autores (Authors)**
   - Crear autor
   - Listar autores (con paginación)
   - Obtener autor por ID
   - Actualizar autor
   - Eliminar autor

2. **Libros (Books)**
   - Crear libro (asociado a un autor)
   - Listar libros (con filtros y paginación)
   - Obtener libro por ID
   - Actualizar libro
   - Eliminar libro

---

## 🗃️ Modelos de Datos

### Author

| Campo | Tipo | Restricciones |
|-------|------|---------------|
| id | int | Primary Key |
| name | str | Required, max 100 |
| country | str | Optional, max 50 |
| created_at | datetime | Default: now |

### Book

| Campo | Tipo | Restricciones |
|-------|------|---------------|
| id | int | Primary Key |
| title | str | Required, max 200 |
| isbn | str | Unique, max 13 |
| year | int | Optional |
| author_id | int | Foreign Key → authors.id |
| created_at | datetime | Default: now |

---

## 📁 Estructura del Proyecto

```
starter/
├── main.py          # FastAPI app y endpoints
├── database.py      # Configuración SQLAlchemy
├── models.py        # Modelos Author y Book
├── schemas.py       # Schemas Pydantic
└── library.db       # SQLite (se crea automáticamente)
```

---

## 🔧 Setup

```bash
cd starter

# Crear entorno con uv
uv init .
uv add fastapi uvicorn sqlalchemy pydantic-settings

# Ejecutar
uv run fastapi dev main.py
```

---

## 📝 Endpoints Requeridos

### Authors

| Método | Ruta | Descripción |
|--------|------|-------------|
| POST | `/authors` | Crear autor |
| GET | `/authors` | Listar autores |
| GET | `/authors/{id}` | Obtener autor |
| PUT | `/authors/{id}` | Actualizar autor |
| DELETE | `/authors/{id}` | Eliminar autor |

### Books

| Método | Ruta | Descripción |
|--------|------|-------------|
| POST | `/books` | Crear libro |
| GET | `/books` | Listar libros |
| GET | `/books/{id}` | Obtener libro |
| PUT | `/books/{id}` | Actualizar libro |
| DELETE | `/books/{id}` | Eliminar libro |

---

## ✅ Criterios de Evaluación

### Funcionalidad (40%)

- [ ] CRUD completo de autores funciona
- [ ] CRUD completo de libros funciona
- [ ] Los libros se asocian correctamente a autores
- [ ] La paginación funciona en listados

### Código (30%)

- [ ] Modelos SQLAlchemy bien definidos
- [ ] Schemas Pydantic con validaciones
- [ ] Dependency Injection con `get_db()`
- [ ] Manejo de errores con HTTPException

### Calidad (30%)

- [ ] Código limpio y organizado
- [ ] Documentación en Swagger funcional
- [ ] Sin errores de linting
- [ ] Respuestas HTTP correctas (201, 404, etc.)

---

## 💡 Hints

### 1. Foreign Key en SQLAlchemy

```python
from sqlalchemy import ForeignKey

class Book(Base):
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
```

### 2. Validar que el autor existe antes de crear libro

```python
@app.post("/books")
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    # Verificar que el autor existe
    author = db.get(Author, book.author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    # ... crear libro
```

### 3. Filtrar libros por autor

```python
@app.get("/books")
def list_books(author_id: int | None = None, db: Session = Depends(get_db)):
    stmt = select(Book)
    if author_id:
        stmt = stmt.where(Book.author_id == author_id)
    # ...
```

---

## 🧪 Probar la API

### Crear autor

```bash
curl -X POST http://localhost:8000/authors \
  -H "Content-Type: application/json" \
  -d '{"name": "Gabriel García Márquez", "country": "Colombia"}'
```

### Crear libro

```bash
curl -X POST http://localhost:8000/books \
  -H "Content-Type: application/json" \
  -d '{"title": "Cien años de soledad", "isbn": "9780060883287", "year": 1967, "author_id": 1}'
```

### Listar libros de un autor

```bash
curl "http://localhost:8000/books?author_id=1"
```

---

## 📤 Entrega

1. Completa todos los TODOs en los archivos `starter/`
2. Verifica que todos los endpoints funcionan
3. Prueba con Swagger UI (http://localhost:8000/docs)
4. Asegúrate de que no hay errores

---

[← Volver a Semana 05](../README.md)
