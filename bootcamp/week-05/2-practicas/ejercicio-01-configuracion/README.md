# 🔧 Ejercicio 01: Configuración SQLAlchemy

## 🎯 Objetivo

Aprender a configurar SQLAlchemy: crear Engine, Session y Base declarativa.

**Duración estimada:** 30 minutos

---

## 📋 Pasos

### Paso 1: Crear el Engine

El **Engine** es la conexión a la base de datos:

```python
from sqlalchemy import create_engine

# SQLite guarda datos en un archivo local
engine = create_engine("sqlite:///./test.db", echo=True)
```

- `sqlite:///./test.db` → archivo `test.db` en directorio actual
- `echo=True` → muestra SQL generado (útil para debug)

**Abre `starter/main.py`** y descomenta la sección del Paso 1.

---

### Paso 2: Crear la Base Declarativa

La **Base** es la clase padre de todos los modelos:

```python
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass
```

**Descomenta** la sección del Paso 2 en `starter/main.py`.

---

### Paso 3: Crear un Modelo Simple

Un modelo representa una tabla:

```python
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

class Item(Base):
    __tablename__ = "items"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
```

**Descomenta** la sección del Paso 3.

---

### Paso 4: Crear las Tablas

SQLAlchemy crea las tablas con `create_all()`:

```python
Base.metadata.create_all(bind=engine)
```

**Descomenta** la sección del Paso 4.

---

### Paso 5: Configurar SessionLocal

El **sessionmaker** crea sesiones configuradas:

```python
from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
```

**Descomenta** la sección del Paso 5.

---

### Paso 6: Probar la Sesión

Usa la sesión para insertar y consultar:

```python
with SessionLocal() as session:
    item = Item(name="Test Item")
    session.add(item)
    session.commit()
    print(f"Item creado con ID: {item.id}")
```

**Descomenta** la sección del Paso 6.

---

## ▶️ Ejecutar

```bash
uv run python starter/main.py
```

**Salida esperada:**
```
=== Paso 1: Engine creado ===
=== Paso 2: Base declarativa lista ===
=== Paso 3: Modelo Item definido ===
=== Paso 4: Tablas creadas ===
=== Paso 5: SessionLocal configurado ===
=== Paso 6: Probando sesión ===
Item creado con ID: 1
Items en DB: [Item(id=1, name='Test Item')]
```

También verás un archivo `test.db` creado.

---

## ✅ Verificación

- [ ] El archivo `test.db` se creó
- [ ] El Engine muestra SQL en consola (`echo=True`)
- [ ] El Item se guardó con ID auto-generado
- [ ] Puedes consultar el Item guardado

---

## 🧠 Conceptos Clave

| Componente | Propósito |
|------------|-----------|
| `Engine` | Conexión a la base de datos |
| `DeclarativeBase` | Clase padre para modelos |
| `sessionmaker` | Factory de sesiones |
| `Session` | Unidad de trabajo para transacciones |

---

[← Volver a Prácticas](../README.md) | [Siguiente: Modelos Declarativos →](../ejercicio-02-modelos/)
