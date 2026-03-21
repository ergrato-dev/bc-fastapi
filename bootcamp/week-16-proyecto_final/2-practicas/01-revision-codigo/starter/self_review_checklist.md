# 📋 Self-Review Checklist

Usa este checklist para revisar tu proyecto final antes de la entrega.

---

## 📁 Estructura del Proyecto

### Organización
- [ ] Estructura de carpetas clara y consistente
- [ ] Separación de capas (routers, services, repositories, models)
- [ ] Archivos `__init__.py` donde corresponde
- [ ] No hay archivos huérfanos o sin usar

### Nombrado
- [ ] Nombres de archivos en snake_case
- [ ] Nombres descriptivos (no `utils2.py` o `helpers_new.py`)
- [ ] Consistencia en nombres (no mezclar `user_service` y `ProductService`)

---

## 🐍 Código Python

### Type Hints
- [ ] Todas las funciones tienen type hints de parámetros
- [ ] Todas las funciones tienen type hints de retorno
- [ ] Uso de `|` para unions (no `Union[]`)
- [ ] Uso de tipos genéricos nativos (`list[str]` no `List[str]`)

### Funciones
- [ ] Funciones cortas (< 20 líneas idealmente)
- [ ] Una responsabilidad por función
- [ ] Nombres descriptivos (verbos para acciones)
- [ ] Sin efectos secundarios inesperados

### Clases
- [ ] Una responsabilidad por clase
- [ ] Métodos relacionados agrupados
- [ ] Uso apropiado de herencia vs composición
- [ ] Dataclasses o Pydantic para DTOs

### Async
- [ ] `async def` para funciones con I/O
- [ ] `await` en todas las llamadas async
- [ ] No mezclar sync y async innecesariamente

---

## 🔒 Seguridad

### Autenticación
- [ ] Passwords hasheados (bcrypt/argon2)
- [ ] Tokens JWT con expiración corta
- [ ] Refresh tokens implementados
- [ ] Logout invalida tokens

### Autorización
- [ ] Verificación de permisos en cada endpoint protegido
- [ ] Usuarios solo acceden a sus propios recursos
- [ ] Roles implementados correctamente

### Inputs
- [ ] Todos los inputs validados con Pydantic
- [ ] Sin SQL injection (uso de ORM)
- [ ] Sin XSS (escapado de outputs si aplica)

### Secrets
- [ ] No hay secrets hardcodeados
- [ ] `.env` en `.gitignore`
- [ ] `.env.example` con placeholders

---

## 🗄️ Base de Datos

### Modelos
- [ ] Campos con tipos apropiados
- [ ] Constraints definidos (unique, not null)
- [ ] Índices en campos frecuentemente consultados
- [ ] Relaciones bien definidas

### Queries
- [ ] Sin N+1 queries
- [ ] Uso de `select_related`/`joinedload` donde aplica
- [ ] Paginación en listados
- [ ] Transactions donde necesario

### Migraciones
- [ ] Alembic configurado
- [ ] Migraciones up-to-date
- [ ] Migraciones revisadas antes de aplicar

---

## 🧪 Testing

### Cobertura
- [ ] Tests para endpoints principales
- [ ] Tests para lógica de negocio crítica
- [ ] Coverage > 50% (idealmente > 70%)

### Calidad
- [ ] Tests independientes entre sí
- [ ] Fixtures para datos de prueba
- [ ] Nombres descriptivos de tests
- [ ] Un assert principal por test

### Ejecución
- [ ] Todos los tests pasan
- [ ] Tests corren en < 1 minuto
- [ ] Tests pueden correr en paralelo

---

## 📝 Documentación

### README
- [ ] Descripción clara del proyecto
- [ ] Requisitos de instalación
- [ ] Instrucciones para correr localmente
- [ ] Variables de entorno documentadas
- [ ] Endpoints principales listados

### API
- [ ] Todos los endpoints documentados en OpenAPI
- [ ] Descripciones claras en endpoints
- [ ] Ejemplos en schemas
- [ ] Códigos de error documentados

### Código
- [ ] Docstrings en funciones públicas complejas
- [ ] Comentarios solo donde necesario
- [ ] No hay TODOs pendientes críticos

---

## 🐳 DevOps

### Docker
- [ ] Dockerfile funciona
- [ ] Multi-stage build
- [ ] Usuario no-root
- [ ] `.dockerignore` configurado

### Docker Compose
- [ ] Servicios bien configurados
- [ ] Health checks definidos
- [ ] Volúmenes para persistencia
- [ ] Networks apropiadas

### CI/CD
- [ ] Pipeline corre en cada push
- [ ] Lint check incluido
- [ ] Tests incluidos
- [ ] Build de Docker exitoso

---

## 🚀 Deployment

### Producción
- [ ] App desplegada y accesible
- [ ] HTTPS habilitado
- [ ] Base de datos externa configurada
- [ ] Variables de entorno en producción

### Monitoreo
- [ ] Health endpoints funcionando
- [ ] Logs accesibles
- [ ] Errores reportados

---

## 📊 Resumen de Revisión

| Categoría | Puntos OK | Total | Porcentaje |
|-----------|-----------|-------|------------|
| Estructura | /6 | 6 | % |
| Código Python | /12 | 12 | % |
| Seguridad | /12 | 12 | % |
| Base de Datos | /9 | 9 | % |
| Testing | /9 | 9 | % |
| Documentación | /9 | 9 | % |
| DevOps | /9 | 9 | % |
| Deployment | /6 | 6 | % |
| **TOTAL** | **/72** | **72** | **%** |

---

## 🎯 Mejoras Identificadas

Lista al menos 5 mejoras que harías con más tiempo:

1. 
2. 
3. 
4. 
5. 

---

## 📝 Notas Adicionales

Usa este espacio para documentar decisiones técnicas, trade-offs, o áreas que requieren atención futura:

```
[Tus notas aquí]
```
