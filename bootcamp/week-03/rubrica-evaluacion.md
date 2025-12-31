# 📊 Rúbrica de Evaluación - Semana 03

## 🎯 Competencias a Evaluar

| Competencia | Descripción |
|-------------|-------------|
| **Diseño de APIs** | Crear rutas RESTful bien estructuradas |
| **Path Parameters** | Usar parámetros de ruta con validación |
| **Query Parameters** | Implementar filtrado y paginación |
| **Integración** | Combinar múltiples fuentes de parámetros |

---

## 📝 Evidencias de Aprendizaje

### 1. Conocimiento (30%)

| Criterio | Excelente (100%) | Bueno (80%) | Suficiente (60%) | Insuficiente (<60%) |
|----------|------------------|-------------|------------------|---------------------|
| Métodos HTTP | Identifica y usa correctamente GET, POST, PUT, PATCH, DELETE | Usa 4 de 5 métodos correctamente | Usa 3 métodos correctamente | Confunde métodos HTTP |
| Diseño RESTful | URLs siguen convenciones REST | URLs mayormente RESTful | Algunas URLs no siguen convenciones | URLs no siguen REST |
| Parámetros | Distingue path, query, body, header | Distingue 3 de 4 tipos | Distingue 2 tipos | No distingue tipos |

### 2. Desempeño (40%)

| Criterio | Excelente (100%) | Bueno (80%) | Suficiente (60%) | Insuficiente (<60%) |
|----------|------------------|-------------|------------------|---------------------|
| Path params | Tipado correcto, validación con Path() | Tipado correcto, validación básica | Solo tipado básico | Sin tipado |
| Query params | Opcionales, defaults, múltiples valores | Opcionales con defaults | Solo parámetros básicos | Sin query params |
| Paginación | Paginación completa con metadatos | Paginación funcional | Paginación básica | Sin paginación |
| Filtros | Filtros múltiples y combinables | Filtros básicos | Un solo filtro | Sin filtros |

### 3. Producto (30%)

| Criterio | Excelente (100%) | Bueno (80%) | Suficiente (60%) | Insuficiente (<60%) |
|----------|------------------|-------------|------------------|---------------------|
| Funcionalidad | Todos los endpoints funcionan correctamente | 90% endpoints funcionan | 70% endpoints funcionan | <70% endpoints |
| Validación | Validación completa con mensajes claros | Validación en la mayoría | Validación básica | Sin validación |
| Documentación | OpenAPI completo con ejemplos | OpenAPI con descripciones | OpenAPI básico | Sin documentación |
| Código | Limpio, organizado, siguiendo convenciones | Mayormente limpio | Algunas inconsistencias | Código desorganizado |

---

## 🏆 Escala de Calificación

| Nivel | Rango | Descripción |
|-------|-------|-------------|
| Excelente | 90-100% | Dominio completo de los conceptos |
| Bueno | 80-89% | Buen entendimiento con detalles menores |
| Suficiente | 70-79% | Cumple requisitos mínimos |
| Insuficiente | <70% | Necesita refuerzo |

---

## ✅ Checklist de Evaluación

### Rutas y Métodos
- [ ] Usa GET para lectura
- [ ] Usa POST para creación
- [ ] Usa PUT/PATCH para actualización
- [ ] Usa DELETE para eliminación
- [ ] URLs siguen convenciones REST

### Path Parameters
- [ ] Parámetros tipados correctamente
- [ ] Usa Path() para validación
- [ ] Maneja IDs inexistentes (404)
- [ ] Soporta múltiples path params

### Query Parameters
- [ ] Parámetros opcionales con defaults
- [ ] Usa Query() para validación
- [ ] Implementa paginación (page, per_page)
- [ ] Implementa filtrado
- [ ] Implementa ordenamiento

### Integración
- [ ] Combina path + query params
- [ ] Combina params + body
- [ ] Documentación OpenAPI correcta
- [ ] Ejemplos en Swagger

---

## 📋 Criterios del Proyecto

### API de Catálogo de Productos

| Requisito | Puntos |
|-----------|--------|
| CRUD de productos | 20 |
| CRUD de categorías | 15 |
| Búsqueda por nombre | 10 |
| Filtro por categoría | 10 |
| Filtro por rango de precio | 10 |
| Paginación | 15 |
| Ordenamiento | 10 |
| Documentación OpenAPI | 10 |
| **Total** | **100** |

---

## 🔗 Recursos de Evaluación

- [FastAPI Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/)
- [FastAPI Query Parameters](https://fastapi.tiangolo.com/tutorial/query-params/)
- [REST API Design Best Practices](https://restfulapi.net/)

---

[← Volver al README](README.md)
