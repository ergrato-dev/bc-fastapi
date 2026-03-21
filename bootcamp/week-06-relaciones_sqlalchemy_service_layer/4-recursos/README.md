# 📚 Recursos - Semana 06

## 🔗 Documentación Oficial

### SQLAlchemy

- [SQLAlchemy ORM Tutorial](https://docs.sqlalchemy.org/en/20/orm/tutorial.html) - Tutorial oficial del ORM
- [Relationship Configuration](https://docs.sqlalchemy.org/en/20/orm/relationships.html) - Configuración de relaciones
- [Basic Relationship Patterns](https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html) - Patrones 1:1, 1:N, N:M
- [Relationship Loading Techniques](https://docs.sqlalchemy.org/en/20/orm/loading_relationships.html) - Eager vs Lazy loading
- [Querying Joined Tables](https://docs.sqlalchemy.org/en/20/orm/queryguide/relationships.html) - Queries con JOINs

### FastAPI

- [FastAPI SQL Databases](https://fastapi.tiangolo.com/tutorial/sql-databases/) - Integración con SQLAlchemy
- [Bigger Applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/) - Estructura con routers
- [Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/) - Sistema de dependencias

### Pydantic

- [Nested Models](https://docs.pydantic.dev/latest/concepts/models/#nested-models) - Modelos anidados
- [Model Config](https://docs.pydantic.dev/latest/api/config/) - from_attributes para ORM

---

## 📖 Artículos Recomendados

### Relaciones en SQLAlchemy

| Artículo | Descripción |
|----------|-------------|
| [SQLAlchemy Relationships](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/) | Tutorial completo de relaciones |
| [Many-to-Many in SQLAlchemy](https://www.digitalocean.com/community/tutorials/how-to-use-many-to-many-database-relationships-with-flask-sqlalchemy) | Guía N:M con ejemplos |
| [N+1 Problem Explained](https://planetscale.com/blog/what-is-n-1-query-problem-and-how-to-solve-it) | El problema N+1 y soluciones |

### Arquitectura Service Layer

| Artículo | Descripción |
|----------|-------------|
| [Service Layer Pattern](https://martinfowler.com/eaaCatalog/serviceLayer.html) | Martin Fowler - definición original |
| [Clean Architecture in Python](https://www.thedigitalcatonline.com/blog/2016/11/14/clean-architectures-in-python-a-step-by-step-example/) | Arquitectura limpia paso a paso |
| [Repository vs Service Layer](https://medium.com/@hathibelagal/the-repository-pattern-vs-the-service-pattern-91f85a4b0b4e) | Diferencias y cuándo usar cada uno |

---

## 🎬 Videografía

### SQLAlchemy Relationships

| Video | Canal | Duración |
|-------|-------|----------|
| [SQLAlchemy Relationships Tutorial](https://www.youtube.com/watch?v=VVX7JIWx-ss) | Pretty Printed | 15 min |
| [One-to-Many SQLAlchemy](https://www.youtube.com/watch?v=juPQ04_twtA) | Corey Schafer | 20 min |
| [Many-to-Many SQLAlchemy](https://www.youtube.com/watch?v=OvhoYbjtiKc) | Pretty Printed | 12 min |

### FastAPI Architecture

| Video | Canal | Duración |
|-------|-------|----------|
| [FastAPI Best Practices](https://www.youtube.com/watch?v=0sOvCWFmrtA) | ArjanCodes | 25 min |
| [Clean Architecture FastAPI](https://www.youtube.com/watch?v=Cy9fAvsXGZA) | TechWorld with Nana | 30 min |
| [FastAPI Project Structure](https://www.youtube.com/watch?v=MFfhjPrtoYQ) | Eric Roby | 20 min |

---

## 📘 Libros Recomendados

### Gratuitos

- **[SQLAlchemy Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/)** - Tutorial oficial completo
- **[FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)** - Documentación como libro

### De Pago (Referencias)

- **"Architecture Patterns with Python"** - Harry Percival & Bob Gregory
  - Capítulos sobre Service Layer y Repository Pattern
- **"Clean Architecture"** - Robert C. Martin
  - Principios de arquitectura de software

---

## 🛠️ Herramientas Útiles

### Desarrollo

| Herramienta | Uso |
|-------------|-----|
| [DB Browser for SQLite](https://sqlitebrowser.org/) | Visualizar base de datos SQLite |
| [DBeaver](https://dbeaver.io/) | Cliente universal de bases de datos |
| [SQLAlchemy Stubs](https://pypi.org/project/sqlalchemy-stubs/) | Type hints para SQLAlchemy |

### Testing

| Herramienta | Uso |
|-------------|-----|
| [pytest](https://docs.pytest.org/) | Framework de testing |
| [Factory Boy](https://factoryboy.readthedocs.io/) | Factories para tests |
| [Faker](https://faker.readthedocs.io/) | Datos falsos para tests |

---

## 🔗 Repositorios de Referencia

| Repositorio | Descripción |
|-------------|-------------|
| [fastapi-best-practices](https://github.com/zhanymkanov/fastapi-best-practices) | Mejores prácticas FastAPI |
| [full-stack-fastapi-template](https://github.com/tiangolo/full-stack-fastapi-template) | Template oficial de Tiangolo |
| [fastapi-sqlalchemy-example](https://github.com/jonra1993/fastapi-alembic-sqlmodel-async) | Ejemplo con SQLAlchemy async |

---

## 📌 Cheatsheets

### SQLAlchemy Relationships

```python
# 1:N - Un autor tiene muchos posts
class Author(Base):
    posts = relationship("Post", back_populates="author")

class Post(Base):
    author_id = Column(ForeignKey("authors.id"))
    author = relationship("Author", back_populates="posts")

# N:M - Posts tienen muchos tags y viceversa
post_tags = Table("post_tags", Base.metadata,
    Column("post_id", ForeignKey("posts.id")),
    Column("tag_id", ForeignKey("tags.id"))
)

class Post(Base):
    tags = relationship("Tag", secondary=post_tags, back_populates="posts")

class Tag(Base):
    posts = relationship("Post", secondary=post_tags, back_populates="tags")
```

### Eager Loading

```python
# joinedload - para relaciones 1:1 o N:1
stmt = select(Post).options(joinedload(Post.author))

# selectinload - para relaciones 1:N o N:M
stmt = select(Author).options(selectinload(Author.posts))

# Combinados
stmt = select(Post).options(
    joinedload(Post.author),
    selectinload(Post.tags)
)
```

---

> 💡 **Tip**: Marca los recursos que más te ayuden y revísalos periódicamente para reforzar conceptos.
