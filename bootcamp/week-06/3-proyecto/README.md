# 📝 Proyecto Semana 06: Blog API con Service Layer

## 🎯 Objetivo

Construir una **API completa de Blog** aplicando:
- Relaciones 1:N (Author → Posts)
- Relaciones N:M (Posts ↔ Tags)
- Arquitectura **Service Layer**
- Queries optimizadas con eager loading

---

## 📋 Requisitos Funcionales

### Entidades

| Entidad | Campos | Relaciones |
|---------|--------|------------|
| **Author** | id, name, email, bio, created_at | 1:N con Post |
| **Post** | id, title, content, published, created_at | N:1 con Author, N:M con Tag |
| **Tag** | id, name, slug | N:M con Post |

### Endpoints Requeridos

#### Authors
- `POST /authors` - Crear autor
- `GET /authors` - Listar autores (con paginación)
- `GET /authors/{id}` - Obtener autor con sus posts
- `PUT /authors/{id}` - Actualizar autor
- `DELETE /authors/{id}` - Eliminar autor

#### Posts
- `POST /posts` - Crear post (con tags)
- `GET /posts` - Listar posts (filtrar por author_id, tag, published)
- `GET /posts/{id}` - Obtener post con autor y tags
- `PUT /posts/{id}` - Actualizar post
- `DELETE /posts/{id}` - Eliminar post
- `POST /posts/{id}/publish` - Publicar post
- `POST /posts/{id}/tags/{tag}` - Agregar tag
- `DELETE /posts/{id}/tags/{tag}` - Eliminar tag

#### Tags
- `POST /tags` - Crear tag
- `GET /tags` - Listar tags (con conteo de posts)
- `GET /tags/{slug}/posts` - Posts por tag

---

## 📁 Estructura del Proyecto

```
starter/
├── main.py                  # FastAPI app
├── config.py                # Configuración
├── database.py              # Engine + Session
├── models/
│   ├── __init__.py
│   ├── author.py
│   ├── post.py
│   └── tag.py
├── schemas/
│   ├── __init__.py
│   ├── author.py
│   ├── post.py
│   └── tag.py
├── services/                # 💼 Lógica de negocio
│   ├── __init__.py
│   ├── author_service.py
│   └── post_service.py
├── routers/                 # 🌐 Endpoints
│   ├── __init__.py
│   ├── authors.py
│   ├── posts.py
│   └── tags.py
└── exceptions.py            # Excepciones personalizadas
```

---

## 🚀 Instrucciones

### 1. Configuración Inicial

```bash
cd starter
uv sync  # o pip install -r requirements.txt
```

### 2. Implementar TODOs

El código tiene marcadores `# TODO:` que debes completar:

1. **models/**: Definir relaciones entre entidades
2. **services/**: Implementar lógica de negocio
3. **routers/**: Conectar endpoints con services

### 3. Ejecutar la API

```bash
uvicorn main:app --reload
```

### 4. Probar en `/docs`

Swagger UI estará disponible en `http://localhost:8000/docs`

---

## ✅ Criterios de Evaluación

| Criterio | Puntos |
|----------|--------|
| Modelos con relaciones correctas | 15 |
| Services implementados | 25 |
| Routers funcionando | 20 |
| Queries optimizadas (no N+1) | 15 |
| Manejo de errores | 10 |
| Código limpio y organizado | 15 |
| **Total** | **100** |

---

## 🎯 Retos Opcionales

1. **Búsqueda**: Agregar endpoint `GET /posts/search?q=texto`
2. **Estadísticas**: Endpoint con posts por autor y tag más usado
3. **Tests**: Escribir tests para los services

---

## 📚 Recursos

- [SQLAlchemy Relationships](https://docs.sqlalchemy.org/en/20/orm/relationships.html)
- [FastAPI Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/)
- [Pydantic v2](https://docs.pydantic.dev/latest/)

---

## 🔗 Navegación

[← Volver a Prácticas](../2-practicas/) | [Ver Teoría →](../1-teoria/)
