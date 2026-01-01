# 📋 Rúbrica de Evaluación - Semana 04

## 🎯 Competencias a Evaluar

### Responses y Manejo de Errores en FastAPI

---

## 🧠 Evidencia de Conocimiento (30%)

### Conceptos Teóricos

| Criterio | Insuficiente (0-59) | Suficiente (60-79) | Bueno (80-89) | Excelente (90-100) |
|----------|---------------------|--------------------|--------------|--------------------|
| **Response Models** | No comprende response_model | Usa response_model básico | Aplica exclude_unset, response_model_exclude | Domina todas las opciones de response_model |
| **Status Codes** | Usa solo 200 para todo | Distingue 2xx de 4xx/5xx | Usa códigos semánticos correctos | Aplica códigos según RFC HTTP |
| **Manejo de Errores** | No maneja errores | Usa HTTPException básico | Crea exception handlers | Implementa jerarquía de errores |
| **OpenAPI** | No documenta | Documenta endpoints básicos | Usa tags, descriptions | Documentación completa con ejemplos |

### Evaluación

- [ ] Quiz teórico sobre códigos HTTP
- [ ] Identificar errores en código de ejemplo
- [ ] Explicar flujo de manejo de errores

---

## 💪 Evidencia de Desempeño (40%)

### Ejercicios Prácticos

| Ejercicio | Peso | Criterios de Evaluación |
|-----------|------|------------------------|
| **01 - Response Models** | 25% | Modelos tipados, campos excluidos, alias |
| **02 - Status Codes** | 25% | Códigos correctos para cada operación |
| **03 - Errores** | 30% | HTTPException, handlers personalizados |
| **04 - Documentación** | 20% | OpenAPI completa y clara |

### Criterios de Código

| Criterio | Puntos |
|----------|--------|
| Código funciona correctamente | 40 |
| Response models bien definidos | 20 |
| Códigos de estado apropiados | 15 |
| Errores manejados correctamente | 15 |
| Documentación OpenAPI | 10 |

---

## 📦 Evidencia de Producto (30%)

### Proyecto: API de Gestión de Tareas

#### Requisitos Funcionales

| Requisito | Peso | Descripción |
|-----------|------|-------------|
| **CRUD Tareas** | 30% | Crear, leer, actualizar, eliminar tareas |
| **Response Models** | 25% | Modelos de respuesta para cada operación |
| **Status Codes** | 20% | Códigos HTTP semánticos |
| **Manejo de Errores** | 15% | HTTPException y handlers |
| **Documentación** | 10% | OpenAPI con descripciones |

#### Rúbrica de Calidad

| Nivel | Descripción | Puntos |
|-------|-------------|--------|
| **Excelente** | API completa, bien documentada, errores robustos | 90-100 |
| **Bueno** | API funcional con response models y errores básicos | 80-89 |
| **Suficiente** | API funciona pero documentación incompleta | 60-79 |
| **Insuficiente** | API no funciona o sin manejo de errores | 0-59 |

---

## ✅ Lista de Verificación

### Response Models
- [ ] Usa `response_model` en todos los endpoints
- [ ] Modelos separados para entrada y salida
- [ ] Campos sensibles excluidos de respuestas
- [ ] Alias para nombres de campo en JSON

### Status Codes
- [ ] 200 OK para GET exitoso
- [ ] 201 Created para POST exitoso
- [ ] 204 No Content para DELETE exitoso
- [ ] 400 Bad Request para datos inválidos
- [ ] 404 Not Found para recursos inexistentes
- [ ] 422 Unprocessable Entity para validación

### Manejo de Errores
- [ ] HTTPException con mensajes claros
- [ ] Exception handlers personalizados
- [ ] Formato consistente de errores
- [ ] Logging de errores

### Documentación
- [ ] Título y descripción de API
- [ ] Tags para agrupar endpoints
- [ ] Descripciones en endpoints
- [ ] Ejemplos de request/response

---

## 📊 Cálculo de Nota Final

```
Nota Final = (Conocimiento × 0.30) + (Desempeño × 0.40) + (Producto × 0.30)
```

### Escala de Calificación

| Rango | Calificación | Descripción |
|-------|--------------|-------------|
| 90-100 | A | Excelente - Dominio completo |
| 80-89 | B | Bueno - Competente |
| 70-79 | C | Satisfactorio - Cumple requisitos |
| 60-69 | D | Suficiente - Necesita mejora |
| 0-59 | F | Insuficiente - No aprueba |

---

## 📝 Notas del Evaluador

```
Estudiante: _______________________
Fecha: _______________________

Conocimiento: _____ / 100 × 0.30 = _____
Desempeño:    _____ / 100 × 0.40 = _____  
Producto:     _____ / 100 × 0.30 = _____

NOTA FINAL: _____ / 100

Observaciones:
_________________________________________________
_________________________________________________
```
