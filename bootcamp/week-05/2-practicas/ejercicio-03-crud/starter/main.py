"""
Ejercicio 03: Operaciones CRUD
==============================
Practica Create, Read, Update, Delete con SQLAlchemy 2.0.

Instrucciones:
1. Lee cada sección
2. Descomenta el código paso a paso
3. Ejecuta: uv run python main.py
"""

# ============================================
# PASO 1: Setup con Modelo Task
# ============================================
print("=== Paso 1: Setup completado ===")

# Descomenta las siguientes líneas:
# from sqlalchemy import create_engine, String, select, desc, func
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
#
# engine = create_engine("sqlite:///./crud_test.db", echo=False)
#
# class Base(DeclarativeBase):
#     pass
#
# class Task(Base):
#     __tablename__ = "tasks"
#     
#     id: Mapped[int] = mapped_column(primary_key=True)
#     title: Mapped[str] = mapped_column(String(200))
#     completed: Mapped[bool] = mapped_column(default=False)
#     priority: Mapped[int] = mapped_column(default=1)  # 1-10
#     
#     def __repr__(self) -> str:
#         return f"Task(id={self.id}, title='{self.title}', completed={self.completed}, priority={self.priority})"
#
# # Crear tablas (borra datos anteriores para demo limpia)
# Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)
#
# SessionLocal = sessionmaker(bind=engine)


# ============================================
# PASO 2: CREATE - Crear Registros
# ============================================
print("=== Paso 2: CREATE ===")

# session.add() agrega un objeto para insertar
# session.add_all() agrega múltiples objetos
# session.commit() ejecuta el INSERT en la DB
# session.refresh() recarga el objeto con valores generados (como id)

# Descomenta las siguientes líneas:
# with SessionLocal() as session:
#     # Crear una tarea
#     task1 = Task(title="Learn SQLAlchemy", priority=5)
#     session.add(task1)
#     session.commit()
#     session.refresh(task1)
#     print(f"Creada: {task1}")
#     
#     # Crear múltiples tareas
#     tasks = [
#         Task(title="Practice CRUD operations", priority=4),
#         Task(title="Build FastAPI project", priority=8),
#         Task(title="Write documentation", priority=2),
#     ]
#     session.add_all(tasks)
#     session.commit()
#     print(f"Creadas {len(tasks)} tareas adicionales")


# ============================================
# PASO 3: READ - Obtener por ID
# ============================================
print("=== Paso 3: READ por ID ===")

# session.get(Model, id) busca por primary key
# Retorna None si no encuentra

# Descomenta las siguientes líneas:
# with SessionLocal() as session:
#     # Buscar por ID
#     task = session.get(Task, 1)
#     if task:
#         print(f"Por ID: {task}")
#     else:
#         print("No encontrado")
#     
#     # ID que no existe
#     not_found = session.get(Task, 999)
#     print(f"ID 999: {not_found}")  # None


# ============================================
# PASO 4: READ - Listar con Filtros
# ============================================
print("=== Paso 4: READ con filtros ===")

# select(Model) crea una consulta SELECT
# .where() agrega condiciones WHERE
# .execute() ejecuta la consulta
# .scalars().all() extrae los objetos como lista

# Descomenta las siguientes líneas:
# with SessionLocal() as session:
#     # Todas las tareas
#     stmt = select(Task)
#     all_tasks = session.execute(stmt).scalars().all()
#     print(f"Todas: {len(all_tasks)} tareas")
#     
#     # Solo pendientes (completed=False)
#     stmt = select(Task).where(Task.completed == False)
#     pending = session.execute(stmt).scalars().all()
#     print(f"Pendientes: {len(pending)} tareas")
#     
#     # Prioridad alta (>= 5)
#     stmt = select(Task).where(Task.priority >= 5)
#     high_priority = session.execute(stmt).scalars().all()
#     print(f"Alta prioridad: {len(high_priority)} tareas")
#     
#     # Múltiples condiciones
#     stmt = select(Task).where(
#         Task.completed == False,
#         Task.priority >= 3
#     )
#     filtered = session.execute(stmt).scalars().all()
#     print(f"Pendientes con prioridad >= 3: {len(filtered)} tareas")


# ============================================
# PASO 5: READ - Ordenar y Paginar
# ============================================
print("=== Paso 5: READ ordenar y paginar ===")

# .order_by() ordena resultados (asc por defecto)
# desc() para orden descendente
# .offset(n) salta n registros
# .limit(n) limita a n registros

# Descomenta las siguientes líneas:
# with SessionLocal() as session:
#     # Ordenar por prioridad descendente
#     stmt = select(Task).order_by(desc(Task.priority))
#     sorted_tasks = session.execute(stmt).scalars().all()
#     print(f"Ordenadas por prioridad: {[t.title for t in sorted_tasks]}")
#     
#     # Paginación: página 1, 2 items por página
#     page = 1
#     per_page = 2
#     stmt = select(Task).offset((page - 1) * per_page).limit(per_page)
#     page_tasks = session.execute(stmt).scalars().all()
#     print(f"Página {page} ({per_page} items): {page_tasks}")
#     
#     # Contar total
#     count_stmt = select(func.count()).select_from(Task)
#     total = session.execute(count_stmt).scalar()
#     print(f"Total de tareas: {total}")


# ============================================
# PASO 6: UPDATE - Modificar Registros
# ============================================
print("=== Paso 6: UPDATE ===")

# Para actualizar:
# 1. Obtener el objeto
# 2. Modificar atributos
# 3. commit() para guardar

# Descomenta las siguientes líneas:
# with SessionLocal() as session:
#     # Obtener tarea
#     task = session.get(Task, 1)
#     print(f"Antes: {task}")
#     
#     # Modificar
#     task.completed = True
#     task.priority = 10
#     
#     # Guardar cambios
#     session.commit()
#     session.refresh(task)
#     print(f"Después: {task}")


# ============================================
# PASO 7: DELETE - Eliminar Registros
# ============================================
print("=== Paso 7: DELETE ===")

# session.delete(obj) marca para eliminar
# commit() ejecuta el DELETE

# Descomenta las siguientes líneas:
# with SessionLocal() as session:
#     # Contar antes
#     count_before = session.execute(select(func.count()).select_from(Task)).scalar()
#     
#     # Eliminar última tarea
#     task = session.get(Task, 4)
#     if task:
#         session.delete(task)
#         session.commit()
#         print(f"Eliminada tarea id={task.id}")
#     
#     # Contar después
#     count_after = session.execute(select(func.count()).select_from(Task)).scalar()
#     print(f"Tareas restantes: {count_after}")


# ============================================
# RESUMEN
# ============================================
print("\n=== Resumen CRUD ===")
print("""
SQLAlchemy 2.0 CRUD Operations:

CREATE:
  session.add(obj)        # Agregar uno
  session.add_all([...])  # Agregar varios
  session.commit()        # Guardar en DB

READ:
  session.get(Model, id)  # Por primary key
  select(Model)           # Query builder
  .where(condition)       # Filtrar
  .order_by(column)       # Ordenar
  .offset(n).limit(m)     # Paginar
  .execute().scalars()    # Ejecutar

UPDATE:
  obj.attribute = value   # Modificar
  session.commit()        # Guardar

DELETE:
  session.delete(obj)     # Marcar para eliminar
  session.commit()        # Ejecutar DELETE
""")
