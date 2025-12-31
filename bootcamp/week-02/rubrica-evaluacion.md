# 📊 Rúbrica de Evaluación - Semana 02

## 🎯 Competencias a Evaluar

| Competencia | Descripción |
|-------------|-------------|
| **Modelado de Datos** | Capacidad de crear modelos Pydantic correctos |
| **Validación** | Implementación de validadores personalizados |
| **Integración** | Uso correcto de Pydantic con FastAPI |
| **Buenas Prácticas** | Código limpio, tipado, documentación |

---

## 📝 Evidencias de Aprendizaje

### 1. Conocimiento (30%) 🧠

| Criterio | Puntos | Descripción |
|----------|--------|-------------|
| Cuestionario teórico | 15 | Preguntas sobre Pydantic v2 |
| Explicación de conceptos | 15 | Diferencia entre validadores, uso de Field |

#### Preguntas de Evaluación

1. ¿Cuál es la diferencia entre `@field_validator` y `@model_validator`?
2. ¿Qué hace `model_config = ConfigDict(str_strip_whitespace=True)`?
3. ¿Cómo se define un campo opcional con valor por defecto?
4. ¿Qué ventaja tiene usar `EmailStr` sobre `str`?
5. ¿Cuándo usar `mode='before'` vs `mode='after'` en validadores?

---

### 2. Desempeño (40%) 💪

| Criterio | Puntos | Descripción |
|----------|--------|-------------|
| Ejercicio 01: BaseModel | 10 | Modelos básicos correctos |
| Ejercicio 02: Field | 10 | Configuración de campos |
| Ejercicio 03: Validadores | 10 | Validadores funcionando |
| Ejercicio 04: Integración | 10 | Pydantic + FastAPI |

#### Criterios de Evaluación por Ejercicio

**Ejercicio 01 - BaseModel:**
- [ ] Modelos con type hints correctos
- [ ] Herencia de modelos implementada
- [ ] Campos opcionales bien definidos

**Ejercicio 02 - Field:**
- [ ] Uso de `Field()` con validaciones
- [ ] Alias configurados correctamente
- [ ] Valores por defecto apropiados

**Ejercicio 03 - Validadores:**
- [ ] `@field_validator` implementado
- [ ] `@model_validator` funcionando
- [ ] Manejo de errores de validación

**Ejercicio 04 - Integración:**
- [ ] Request models en endpoints
- [ ] Response models configurados
- [ ] Validación automática funcionando

---

### 3. Producto (30%) 📦

| Criterio | Puntos | Descripción |
|----------|--------|-------------|
| Funcionalidad | 15 | API funciona correctamente |
| Validación | 10 | Todas las validaciones implementadas |
| Documentación | 5 | Código documentado, OpenAPI completo |

#### Proyecto: API de Gestión de Usuarios

**Requisitos Mínimos (Aprobatorio):**
- [ ] Modelo `User` con validaciones básicas
- [ ] Endpoint POST `/users` funcionando
- [ ] Endpoint GET `/users/{id}` funcionando
- [ ] Validación de email formato correcto

**Requisitos Completos (Competente):**
- [ ] Validación de contraseña segura
- [ ] Modelo `UserCreate` y `UserResponse` separados
- [ ] Endpoints CRUD completos
- [ ] Mensajes de error claros

**Requisitos Avanzados (Destacado):**
- [ ] Validador de email único
- [ ] Modelo `UserUpdate` con campos opcionales
- [ ] Paginación en listado
- [ ] Tests de validación

---

## 📈 Escala de Calificación

| Nivel | Rango | Descripción |
|-------|-------|-------------|
| 🥉 **Básico** | 60-69% | Cumple requisitos mínimos |
| 🥈 **Competente** | 70-84% | Cumple todos los requisitos |
| 🥇 **Destacado** | 85-100% | Supera expectativas |

---

## ✅ Lista de Verificación Final

Antes de entregar, verifica:

- [ ] Todos los ejercicios ejecutan sin errores
- [ ] El proyecto tiene todas las validaciones requeridas
- [ ] Los endpoints retornan respuestas correctas
- [ ] La documentación en `/docs` está completa
- [ ] El código tiene type hints en todas las funciones
- [ ] Los modelos Pydantic tienen docstrings

---

## 🚨 Errores Comunes a Evitar

| Error | Solución |
|-------|----------|
| Olvidar `from __future__ import annotations` | No necesario en Python 3.10+ |
| Usar `Optional[X]` en lugar de `X \| None` | Preferir sintaxis moderna |
| No manejar errores de validación | Usar `ValidationError` |
| Campos mutables como default | Usar `Field(default_factory=list)` |
| Validador que no retorna valor | Siempre retornar el valor validado |

---

## 📅 Fecha de Entrega

- **Ejercicios**: Durante la semana
- **Proyecto**: Final de la semana
- **Cuestionario**: Última sesión

---

[← Volver a Semana 02](README.md)
