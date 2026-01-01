# 📤 Semana 04: Responses y Manejo de Errores

## 🎯 Objetivos de la Semana

Al finalizar esta semana, serás capaz de:

- ✅ Definir modelos de respuesta tipados con `response_model`
- ✅ Usar códigos de estado HTTP correctamente
- ✅ Implementar manejo de errores con HTTPException
- ✅ Crear exception handlers personalizados
- ✅ Documentar APIs con OpenAPI/Swagger

---

## 📚 Contenido

### 1. Teoría

| Archivo | Tema | Duración |
|---------|------|----------|
| [01-response-models.md](1-teoria/01-response-models.md) | Response models, tipado de respuestas | 25 min |
| [02-status-codes.md](1-teoria/02-status-codes.md) | Códigos HTTP, cuándo usar cada uno | 25 min |
| [03-manejo-errores.md](1-teoria/03-manejo-errores.md) | HTTPException, validación, errores | 25 min |
| [04-responses-avanzadas.md](1-teoria/04-responses-avanzadas.md) | JSONResponse, RedirectResponse, streaming | 25 min |
| [05-documentacion-openapi.md](1-teoria/05-documentacion-openapi.md) | OpenAPI, Swagger UI, ReDoc | 20 min |

### 2. Prácticas

| Ejercicio | Descripción | Duración |
|-----------|-------------|----------|
| [ejercicio-01](2-practicas/ejercicio-01-response-models/) | Modelos de respuesta tipados | 30 min |
| [ejercicio-02](2-practicas/ejercicio-02-status-codes/) | Códigos de estado apropiados | 35 min |
| [ejercicio-03](2-practicas/ejercicio-03-errores/) | Manejo de errores y excepciones | 40 min |
| [ejercicio-04](2-practicas/ejercicio-04-documentacion/) | Documentación OpenAPI | 35 min |

### 3. Proyecto

[**API de Gestión de Tareas (Task Manager)**](3-proyecto/)

API completa con:
- Modelos de respuesta bien definidos
- Códigos de estado semánticos
- Manejo robusto de errores
- Documentación completa en OpenAPI

---

## ⏱️ Distribución del Tiempo

| Actividad | Tiempo |
|-----------|--------|
| Teoría | 2 horas |
| Prácticas | 2.5 horas |
| Proyecto | 1.5 horas |
| **Total** | **6 horas** |

---

## 📋 Requisitos Previos

- ✅ Semana 01: Fundamentos de FastAPI
- ✅ Semana 02: Pydantic v2
- ✅ Semana 03: Rutas y Parámetros

---

## 🗂️ Estructura de la Semana

```
week-04/
├── README.md
├── rubrica-evaluacion.md
├── 0-assets/
│   ├── 01-response-flow.svg
│   ├── 02-status-codes.svg
│   └── 03-error-handling.svg
├── 1-teoria/
│   ├── 01-response-models.md
│   ├── 02-status-codes.md
│   ├── 03-manejo-errores.md
│   ├── 04-responses-avanzadas.md
│   └── 05-documentacion-openapi.md
├── 2-practicas/
│   ├── README.md
│   ├── ejercicio-01-response-models/
│   ├── ejercicio-02-status-codes/
│   ├── ejercicio-03-errores/
│   └── ejercicio-04-documentacion/
├── 3-proyecto/
│   ├── README.md
│   ├── starter/
│   └── solution/
├── 4-recursos/
│   ├── README.md
│   ├── videografia/
│   └── webgrafia/
└── 5-glosario/
    └── README.md
```

---

## 🔗 Navegación

| Anterior | Siguiente |
|----------|-----------|
| [← Semana 03: Rutas y Parámetros](../week-03/README.md) | [Semana 05: Modelos Complejos →](../week-05/README.md) |

---

## 🏆 Criterios de Evaluación

Ver [rubrica-evaluacion.md](rubrica-evaluacion.md) para los criterios detallados.

| Evidencia | Peso |
|-----------|------|
| 🧠 Conocimiento | 30% |
| 💪 Desempeño | 40% |
| 📦 Producto | 30% |
