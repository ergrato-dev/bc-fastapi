# 🛠️ Prácticas - Semana 05

## 📋 Índice de Ejercicios

| # | Ejercicio | Tema | Duración |
|---|-----------|------|----------|
| 01 | [Configuración SQLAlchemy](01-ejercicio-configuracion/) | Engine, Session, Base | 30 min |
| 02 | [Modelos Declarativos](02-ejercicio-modelos/) | Mapped, mapped_column, tipos | 40 min |
| 03 | [Operaciones CRUD](03-ejercicio-crud/) | Create, Read, Update, Delete | 45 min |
| 04 | [FastAPI + Database](04-ejercicio-fastapi-db/) | Dependency Injection, endpoints | 45 min |

**Tiempo total estimado:** ~2.5 horas

---

## 🎯 Objetivo

Practicar los conceptos de SQLAlchemy ORM vistos en la teoría mediante ejercicios guiados paso a paso.

---

## 📝 Formato de los Ejercicios

Cada ejercicio es un **tutorial guiado**:

1. Lee las instrucciones en el `README.md` del ejercicio
2. Abre el archivo `starter/main.py`
3. **Descomenta** el código según las instrucciones
4. Ejecuta y verifica que funciona

> ⚠️ **Importante**: El código ya está escrito y comentado. Tu tarea es descomentarlo, entenderlo y verificar que funciona correctamente.

---

## 🔧 Requisitos Previos

Antes de comenzar, asegúrate de tener:

```bash
# Crear entorno con uv
uv init week-05-practicas
cd week-05-practicas

# Agregar dependencias
uv add sqlalchemy fastapi uvicorn pydantic-settings

# Verificar instalación
uv run python -c "import sqlalchemy; print(f'SQLAlchemy {sqlalchemy.__version__}')"
```

---

## 📂 Estructura de Cada Ejercicio

```
ejercicio-XX-nombre/
├── README.md          # Instrucciones paso a paso
└── starter/
    └── main.py        # Código con secciones comentadas
```

---

## ✅ Checklist de Completitud

- [ ] Ejercicio 01: Configuración SQLAlchemy
- [ ] Ejercicio 02: Modelos Declarativos
- [ ] Ejercicio 03: Operaciones CRUD
- [ ] Ejercicio 04: FastAPI + Database

---

[← Volver a Semana 05](../README.md)
