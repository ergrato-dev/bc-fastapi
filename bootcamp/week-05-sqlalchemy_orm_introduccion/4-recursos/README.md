# 📚 Recursos Adicionales - Semana 05

## 📖 Documentación Oficial

### SQLAlchemy

- [SQLAlchemy 2.0 Documentation](https://docs.sqlalchemy.org/en/20/)
- [ORM Quick Start](https://docs.sqlalchemy.org/en/20/orm/quickstart.html)
- [Mapped Column Configuration](https://docs.sqlalchemy.org/en/20/orm/mapped_attributes.html)
- [Session Basics](https://docs.sqlalchemy.org/en/20/orm/session_basics.html)

### FastAPI + SQLAlchemy

- [FastAPI SQL Databases](https://fastapi.tiangolo.com/tutorial/sql-databases/)
- [FastAPI Dependency Injection](https://fastapi.tiangolo.com/tutorial/dependencies/)

### Pydantic

- [Pydantic V2 Documentation](https://docs.pydantic.dev/latest/)
- [Model Config - from_attributes](https://docs.pydantic.dev/latest/concepts/models/#model-config)

---

## 🎥 Videos Recomendados

### SQLAlchemy 2.0

1. **SQLAlchemy 2.0 - The New Way**
   - Canal: ArjanCodes
   - Duración: ~20 min
   - Tema: Migración a SQLAlchemy 2.0

2. **FastAPI with SQLAlchemy Full Tutorial**
   - Canal: TechWithTim
   - Duración: ~45 min
   - Tema: Integración completa

### ORM Concepts

3. **What is an ORM?**
   - Canal: Fireship
   - Duración: ~5 min
   - Tema: Conceptos básicos de ORM

---

## 📘 Artículos

### Introductorios

- [Understanding ORMs](https://www.fullstackpython.com/object-relational-mappers-orms.html)
- [SQLAlchemy ORM vs Core](https://docs.sqlalchemy.org/en/20/orm/queryguide/api_comparison.html)

### Avanzados

- [SQLAlchemy 2.0 Migration Guide](https://docs.sqlalchemy.org/en/20/changelog/migration_20.html)
- [Async SQLAlchemy](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html)

---

## 🔗 Herramientas Útiles

### Visualizar SQLite

- [DB Browser for SQLite](https://sqlitebrowser.org/) - GUI para SQLite
- [SQLite Viewer (VS Code Extension)](https://marketplace.visualstudio.com/items?itemName=qwtel.sqlite-viewer)

### Testing

- [pytest-asyncio](https://pytest-asyncio.readthedocs.io/) - Para tests async
- [SQLAlchemy Testing](https://docs.sqlalchemy.org/en/20/orm/session_transaction.html#joining-a-session-into-an-external-transaction-such-as-for-test-suites)

---

## 📝 Cheatsheets

### SQLAlchemy 2.0 Quick Reference

```python
# Engine
engine = create_engine("sqlite:///./app.db")

# Base
class Base(DeclarativeBase):
    pass

# Model
class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

# Session
SessionLocal = sessionmaker(bind=engine)

# CRUD
with SessionLocal() as session:
    # Create
    user = User(name="John")
    session.add(user)
    session.commit()
    
    # Read
    user = session.get(User, 1)
    users = session.execute(select(User)).scalars().all()
    
    # Update
    user.name = "Jane"
    session.commit()
    
    # Delete
    session.delete(user)
    session.commit()
```

---

[← Volver a Semana 05](../README.md)
