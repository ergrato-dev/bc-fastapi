# 📋 Rúbrica de Evaluación - Semana 08

## Arquitectura en Capas Completa

---

## 🎯 Competencias a Evaluar

| Competencia | Peso |
|-------------|------|
| Estructura de proyecto en capas | 25% |
| DTOs y Mappers | 25% |
| Manejo de errores por capa | 25% |
| Proyecto integrador | 25% |

---

## 📊 Criterios de Evaluación

### 1. Estructura de Proyecto en Capas (25%)

#### Excelente (90-100%)
- Separación clara: routers, services, repositories
- Dependencias fluyen en una dirección (hacia abajo)
- Cada capa tiene responsabilidad única
- Imports organizados y sin dependencias circulares

#### Satisfactorio (70-89%)
- Estructura de capas correcta con pequeñas mezclas
- Dependencias mayormente unidireccionales
- Responsabilidades claras en general

#### En Desarrollo (50-69%)
- Estructura parcial, algunas capas mezcladas
- Lógica de negocio en routers
- Acceso directo a DB desde services

#### Insuficiente (<50%)
- Sin separación de capas
- Todo en un archivo o sin organización
- Dependencias circulares

---

### 2. DTOs y Mappers (25%)

#### Excelente (90-100%)
- DTOs específicos para cada operación (Create, Update, Response)
- Mappers para convertir Entity ↔ DTO
- Validaciones en DTOs con Pydantic
- Separación clara entre schemas de API y modelos de DB

#### Satisfactorio (70-89%)
- DTOs implementados correctamente
- Conversiones manuales pero funcionales
- Validaciones básicas presentes

#### En Desarrollo (50-69%)
- DTOs parciales, reúso excesivo
- Sin mappers explícitos
- Exposición de modelos de DB en API

#### Insuficiente (<50%)
- Sin DTOs, modelos expuestos directamente
- Sin validaciones
- Mezcla de responsabilidades

---

### 3. Manejo de Errores por Capa (25%)

#### Excelente (90-100%)
- Excepciones personalizadas por capa
- Traducción de errores entre capas
- Exception handlers centralizados
- Respuestas de error consistentes

#### Satisfactorio (70-89%)
- Excepciones personalizadas implementadas
- Manejo de errores funcional
- Respuestas de error estructuradas

#### En Desarrollo (50-69%)
- Excepciones genéricas
- Errores propagados sin traducir
- Respuestas inconsistentes

#### Insuficiente (<50%)
- Sin manejo de errores
- Errores 500 sin información
- Excepciones no controladas

---

### 4. Proyecto Integrador (25%)

#### Excelente (90-100%)
- Todas las capas implementadas correctamente
- CRUD completo con DTOs
- Tests para services con fakes
- Documentación OpenAPI correcta
- Código limpio y bien organizado

#### Satisfactorio (70-89%)
- Capas implementadas funcionalmente
- CRUD operativo
- Algunos tests
- API documentada

#### En Desarrollo (50-69%)
- Implementación parcial
- CRUD incompleto
- Sin tests
- Documentación básica

#### Insuficiente (<50%)
- Proyecto no funcional
- Sin estructura de capas
- Sin documentación

---

## 📝 Entregables

1. **Prácticas completadas** (4 ejercicios)
2. **Proyecto E-Commerce API** funcional
3. **Tests unitarios** para services
4. **Documentación** de API (OpenAPI)

---

## ✅ Checklist de Autoevaluación

### Estructura
- [ ] Carpetas separadas: routers/, services/, repositories/
- [ ] Schemas en carpeta propia
- [ ] Models separados de schemas
- [ ] Dependencies centralizadas

### DTOs
- [ ] CreateDTO para creación
- [ ] UpdateDTO para actualización (campos opcionales)
- [ ] ResponseDTO para respuestas
- [ ] Mappers implementados

### Errores
- [ ] NotFoundError personalizado
- [ ] ValidationError personalizado
- [ ] ConflictError para duplicados
- [ ] Exception handlers configurados

### Proyecto
- [ ] API funcional con todos los endpoints
- [ ] Tests ejecutándose sin errores
- [ ] Documentación accesible en /docs
- [ ] Código formateado y limpio

---

## 📅 Fecha de Entrega

- **Prácticas**: Durante la semana
- **Proyecto**: Fin de la semana 08
