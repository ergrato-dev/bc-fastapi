# ✅ Semana 2: Pydantic v2 - Validación de Datos

## 🎯 Objetivos de Aprendizaje

Al finalizar esta semana, serás capaz de:

- ✅ Entender qué es Pydantic y por qué es fundamental en FastAPI
- ✅ Crear modelos de datos con `BaseModel`
- ✅ Usar Field para configurar validaciones avanzadas
- ✅ Implementar validadores personalizados (`@field_validator`, `@model_validator`)
- ✅ Trabajar con tipos de datos especiales (EmailStr, HttpUrl, etc.)
- ✅ Configurar modelos con `model_config`
- ✅ Integrar Pydantic con endpoints de FastAPI

---

## 📚 Requisitos Previos

- Haber completado la **Semana 01**
- Entorno Docker configurado
- Conocimiento de type hints en Python
- Familiaridad básica con FastAPI

---

## 🗂️ Estructura de la Semana

```
week-02/
├── README.md                      # Este archivo
├── rubrica-evaluacion.md          # Criterios de evaluación
├── 0-assets/                      # Diagramas y recursos visuales
│   ├── 01-pydantic-validation-flow.svg
│   ├── 02-field-types.svg
│   └── 03-pydantic-fastapi-integration.svg
├── 1-teoria/                      # Material teórico
│   ├── 01-intro-pydantic.md
│   ├── 02-basemodel.md
│   ├── 03-validadores.md
│   ├── 04-field-types.md
│   └── 05-pydantic-fastapi.md
├── 2-practicas/                   # Ejercicios guiados
│   ├── ejercicio-01-basemodel/
│   ├── ejercicio-02-field/
│   ├── ejercicio-03-validadores/
│   └── ejercicio-04-integracion/
├── 3-proyecto/                    # Proyecto semanal
│   ├── starter/
│   └── solution/                  # (gitignored)
├── 4-recursos/                    # Material adicional
│   ├── ebooks-free/
│   ├── videografia/
│   └── webgrafia/
└── 5-glosario/                    # Términos clave
    └── README.md
```

---

## 📝 Contenidos

### 1️⃣ Teoría (1.5-2 horas)

| Tema | Duración | Descripción |
|------|----------|-------------|
| [Introducción a Pydantic](1-teoria/01-intro-pydantic.md) | 20 min | Qué es, por qué usarlo, instalación |
| [BaseModel en Profundidad](1-teoria/02-basemodel.md) | 25 min | Crear modelos, herencia, configuración |
| [Validadores Personalizados](1-teoria/03-validadores.md) | 30 min | field_validator, model_validator |
| [Tipos de Campo Especiales](1-teoria/04-field-types.md) | 20 min | EmailStr, HttpUrl, constr, Field |
| [Pydantic + FastAPI](1-teoria/05-pydantic-fastapi.md) | 25 min | Request/Response models, integración |

### 2️⃣ Prácticas (2-2.5 horas)

| Ejercicio | Duración | Tema |
|-----------|----------|------|
| [01-basemodel](2-practicas/ejercicio-01-basemodel/) | 30 min | Crear modelos básicos |
| [02-field](2-practicas/ejercicio-02-field/) | 30 min | Configurar campos con Field |
| [03-validadores](2-practicas/ejercicio-03-validadores/) | 30 min | Validadores personalizados |
| [04-integracion](2-practicas/ejercicio-04-integracion/) | 30 min | Pydantic en endpoints FastAPI |

### 3️⃣ Proyecto (1.5-2 horas)

**API de Gestión de Usuarios** - Sistema de registro y gestión de usuarios con validación robusta:

- Validación de emails únicos
- Contraseñas seguras con requisitos
- Perfiles de usuario con datos opcionales
- Endpoints CRUD con modelos Pydantic

---

## ⏱️ Distribución del Tiempo

| Actividad | Tiempo |
|-----------|--------|
| 📖 Teoría | 2 horas |
| 💻 Prácticas | 2 horas |
| 🎯 Proyecto | 2 horas |
| **Total** | **6 horas** |

---

## 📌 Entregables

1. **Ejercicios completados** - Código descomentado y funcionando
2. **Proyecto semanal** - API de Gestión de Usuarios
3. **Cuestionario teórico** - Evaluación de conocimientos

---

## 🔑 Conceptos Clave

| Concepto | Descripción |
|----------|-------------|
| `BaseModel` | Clase base para crear modelos de datos |
| `Field` | Configuración avanzada de campos |
| `@field_validator` | Validador para campos individuales |
| `@model_validator` | Validador para el modelo completo |
| `model_config` | Configuración global del modelo |
| `EmailStr` | Tipo para emails validados |
| `constr` | String con restricciones |

---

## 🔗 Navegación

[← Semana 01: Intro Python/FastAPI](../week-01/) | [Semana 03: Pydantic Avanzado →](../week-03/)

---

## 📚 Recursos Adicionales

- [Documentación Oficial Pydantic v2](https://docs.pydantic.dev/latest/)
- [FastAPI - Request Body](https://fastapi.tiangolo.com/tutorial/body/)
- [Pydantic Field Types](https://docs.pydantic.dev/latest/concepts/fields/)
