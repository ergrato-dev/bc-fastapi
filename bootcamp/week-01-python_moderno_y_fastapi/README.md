# 🚀 Semana 1: Introducción a Python Moderno y FastAPI

## 🎯 Objetivos de Aprendizaje

Al finalizar esta semana, serás capaz de:

- ✅ Configurar un entorno de desarrollo con Docker para FastAPI
- ✅ Comprender y usar type hints en Python 3.12+
- ✅ Entender la programación asíncrona con `async`/`await`
- ✅ Crear tu primera API con FastAPI
- ✅ Definir rutas GET y POST básicas
- ✅ Usar parámetros de ruta y query strings
- ✅ Explorar la documentación automática (Swagger/ReDoc)

---

## 📚 Requisitos Previos

- **Docker** y **Docker Compose** instalados ([Bootcamp Docker](https://github.com/ergrato-dev/bc-docker))
- **VS Code** con extensiones recomendadas
- **Git** configurado
- Conocimientos básicos de Python (variables, funciones, estructuras de datos)

---

## 🗂️ Estructura de la Semana

```
week-01-python_moderno_y_fastapi/
├── README.md                      # Este archivo
├── rubrica-evaluacion.md          # Criterios de evaluación
├── 0-assets/                      # Diagramas y recursos visuales
├── 1-teoria/                      # Material teórico
│   ├── 01-entorno-docker.md
│   ├── 02-python-moderno.md
│   ├── 03-type-hints.md
│   ├── 04-async-await.md
│   └── 05-intro-fastapi.md
├── 2-practicas/                   # Ejercicios guiados
│   ├── 01-ejercicio-setup/
│   ├── 02-ejercicio-type-hints/
│   ├── 03-ejercicio-async/
│   └── 04-ejercicio-primera-api/
├── 3-proyecto/                    # Proyecto semanal
│   └── api-saludo/
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

| Tema                                                    | Duración | Descripción                           |
| ------------------------------------------------------- | -------- | ------------------------------------- |
| [Entorno con Docker](1-teoria/01-entorno-docker.md)     | 20 min   | Configurar Docker para desarrollo     |
| [Python Moderno](1-teoria/02-python-moderno.md)         | 25 min   | Características de Python 3.12+       |
| [Type Hints](1-teoria/03-type-hints.md)                 | 25 min   | Tipado estático en Python             |
| [Async/Await](1-teoria/04-async-await.md)               | 25 min   | Programación asíncrona                |
| [Introducción a FastAPI](1-teoria/05-intro-fastapi.md)  | 25 min   | Primera API y conceptos básicos       |

### 2️⃣ Prácticas (2.5-3 horas)

| Ejercicio                 | Duración | Nivel      | Objetivo                              |
| ------------------------- | -------- | ---------- | ------------------------------------- |
| Setup Docker              | 30 min   | Básico     | Levantar entorno de desarrollo        |
| Type Hints                | 45 min   | Básico     | Tipar funciones y variables           |
| Async/Await               | 45 min   | Básico     | Crear funciones asíncronas            |
| Primera API               | 45 min   | Básico     | Endpoints GET y POST con FastAPI      |

### 3️⃣ Proyecto (1.5-2 horas)

**API de Saludo Personalizado**

Crear una API REST básica que:
- Reciba el nombre de un usuario
- Devuelva un saludo personalizado
- Use type hints en todo el código
- Tenga documentación automática
- Corra en Docker

---

## ⏱️ Distribución del Tiempo (6 horas)

```
📖 Teoría:           1.5-2h  (25-33%)
💻 Prácticas:        2.5-3h  (42-50%)
🚀 Proyecto:         1.5-2h  (25-33%)
```

### Cronograma Sugerido

| Día       | Actividad                    | Tiempo |
| --------- | ---------------------------- | ------ |
| **Día 1** | Teoría: Docker + Python      | 1h     |
| **Día 2** | Teoría: Type hints + Async   | 1h     |
| **Día 3** | Ejercicios 1-2               | 1.5h   |
| **Día 4** | Ejercicios 3-4               | 1.5h   |
| **Día 5** | Proyecto final               | 1-2h   |

---

## 📌 Entregable

**Proyecto: [Greeting API](3-proyecto/)**

API de saludo personalizado funcionando en Docker con:

- [ ] Endpoints GET y POST implementados
- [ ] Type hints en todo el código
- [ ] Documentación Swagger accesible en `/docs`
- [ ] Código limpio y comentado en inglés

---

## 🎓 Conceptos Clave

- **Type Hints**: Anotaciones de tipo para variables y funciones
- **Async/Await**: Palabras clave para programación asíncrona
- **FastAPI**: Framework web moderno y rápido para Python
- **Uvicorn**: Servidor ASGI para aplicaciones async
- **OpenAPI**: Especificación para documentar APIs REST
- **Swagger UI**: Interfaz interactiva para probar APIs
- **Docker Compose**: Orquestador de contenedores

---

## 📚 Recursos Adicionales

### 📖 Lecturas Recomendadas

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Python Type Hints - PEP 484](https://peps.python.org/pep-0484/)
- [Real Python: Async IO](https://realpython.com/async-io-python/)

### 🎥 Videos

- Ver carpeta [4-recursos/videografia/](4-recursos/videografia/)

### 🔗 Enlaces Útiles

- Ver carpeta [4-recursos/webgrafia/](4-recursos/webgrafia/)

---

## ✅ Checklist de Verificación

Antes de pasar a la Semana 2, asegúrate de:

- [ ] Tener Docker funcionando con FastAPI
- [ ] Entender la sintaxis de type hints
- [ ] Saber la diferencia entre `def` y `async def`
- [ ] Crear endpoints GET y POST en FastAPI
- [ ] Usar path parameters y query parameters
- [ ] Acceder a la documentación en `/docs`
- [ ] Completar todos los ejercicios prácticos
- [ ] Entregar el proyecto funcional
- [ ] Alcanzar mínimo 70% en cada tipo de evidencia

---

## 🔗 Navegación

⬅️ **Anterior**: [Inicio del Bootcamp](../../README.md)  
➡️ **Siguiente**: [Semana 2: Pydantic y Validación de Datos](../week-02-pydantic_v2_validacion_datos/README.md)

---

## 💡 Consejos para Esta Semana

> 💡 **Docker es tu amigo**: No instales Python localmente. Docker garantiza que todos tengan el mismo entorno.

> 🎯 **Type hints desde el día 1**: Acostúmbrate a tipar todo. FastAPI los usa para validación automática.

> 🚀 **Explora `/docs`**: La documentación automática de FastAPI es increíble. Úsala para probar tus endpoints.

> 🤝 **Pide ayuda**: Si algo no queda claro, usa las Discussions del repositorio.

---

<p align="center">
  <strong>¡Bienvenido al mundo de FastAPI! 🚀</strong><br>
  <em>Esta es la primera semana de un viaje increíble</em>
</p>

<p align="center">
  <a href="1-teoria/01-entorno-docker.md">📖 Comenzar con Teoría</a> •
  <a href="2-practicas/">💻 Ir a Prácticas</a> •
  <a href="3-proyecto/">🚀 Ver Proyecto</a>
</p>
