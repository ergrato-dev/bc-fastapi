# 🏆 Proyecto Final: API Completa Lista para Producción

## 📋 Descripción

Este es tu **proyecto final del bootcamp**. Construirás una API RESTful completa desde cero, aplicando todo lo aprendido durante las 16 semanas.

El proyecto debe demostrar tu dominio de:
- FastAPI y Python moderno
- Arquitectura limpia
- Autenticación y seguridad
- Testing
- Docker y CI/CD
- Documentación profesional

---

## 🎯 Objetivos

1. Construir una API funcional y bien estructurada
2. Implementar autenticación JWT completa
3. Escribir tests con buena cobertura
4. Containerizar con Docker
5. Desplegar a producción
6. Documentar profesionalmente

---

## ⏱️ Tiempo Estimado

~7 horas de trabajo efectivo (distribuidas en la semana)

---

## 📊 Opciones de Proyecto

Elige **UNA** opción. Todas tienen requisitos equivalentes.

### Opción A: Task Management API (Recomendada)

**Tema**: Sistema de gestión de tareas y proyectos

**Entidades**:
| Entidad | Descripción |
|---------|-------------|
| User | Usuarios del sistema |
| Project | Proyectos que contienen tareas |
| Task | Tareas asignables a usuarios |
| Label | Etiquetas para categorizar tareas |

**Relaciones**:
- User 1:N Projects (un usuario tiene muchos proyectos)
- Project 1:N Tasks (un proyecto tiene muchas tareas)
- Task N:1 User (una tarea puede asignarse a un usuario)
- Task N:M Labels (muchos a muchos)

### Opción B: E-commerce API

**Tema**: Tienda online con carrito y pedidos

**Entidades**:
| Entidad | Descripción |
|---------|-------------|
| User | Clientes y administradores |
| Product | Productos de la tienda |
| Category | Categorías de productos |
| Order | Pedidos de clientes |
| OrderItem | Items dentro de un pedido |

### Opción C: Blog API

**Tema**: Plataforma de blogging

**Entidades**:
| Entidad | Descripción |
|---------|-------------|
| User | Autores del blog |
| Post | Artículos publicados |
| Category | Categorías de posts |
| Tag | Etiquetas de posts |
| Comment | Comentarios en posts |

### Opción D: Proyecto Propio

Propón tu idea (debe aprobarse). Requisitos mínimos:
- 4+ entidades con relaciones
- Complejidad similar a las opciones anteriores

---

## ✅ Requisitos Obligatorios

### 1. Arquitectura (20 pts)

```
src/
├── main.py              # Entry point
├── config.py            # Settings con Pydantic
├── database.py          # Configuración de DB
├── models/              # Modelos SQLAlchemy
├── schemas/             # Schemas Pydantic
├── repositories/        # Capa de acceso a datos
├── services/            # Lógica de negocio
├── routers/             # Endpoints API
├── dependencies/        # Dependencies de FastAPI
├── exceptions/          # Excepciones personalizadas
└── utils/               # Utilidades
```

- [ ] Separación clara de capas
- [ ] Inyección de dependencias
- [ ] Código limpio y organizado

### 2. Autenticación y Autorización (20 pts)

**Endpoints requeridos**:
```
POST /api/v1/auth/register   - Registro de usuario
POST /api/v1/auth/login      - Login (retorna tokens)
POST /api/v1/auth/refresh    - Renovar access token
GET  /api/v1/auth/me         - Usuario actual
```

- [ ] JWT con access y refresh tokens
- [ ] Passwords hasheados (bcrypt)
- [ ] Roles: admin, user
- [ ] Protección de endpoints por rol

### 3. CRUD Completo (20 pts)

Para cada entidad principal:
```
GET    /api/v1/{resource}        - Listar (con paginación)
POST   /api/v1/{resource}        - Crear
GET    /api/v1/{resource}/{id}   - Obtener uno
PUT    /api/v1/{resource}/{id}   - Actualizar
DELETE /api/v1/{resource}/{id}   - Eliminar
```

- [ ] Validación de inputs con Pydantic
- [ ] Manejo de errores consistente
- [ ] Paginación en listados
- [ ] Filtros básicos

### 4. Testing (15 pts)

- [ ] Tests de endpoints principales
- [ ] Tests de autenticación
- [ ] Fixtures reutilizables
- [ ] Coverage > 50%

### 5. Docker y CI/CD (15 pts)

- [ ] Dockerfile funcional
- [ ] docker-compose.yml con API + DB
- [ ] GitHub Actions: lint + test
- [ ] Health checks

### 6. Documentación (10 pts)

- [ ] README completo
- [ ] OpenAPI documentado
- [ ] Variables de entorno en .env.example
- [ ] Instrucciones de instalación

---

## 📁 Estructura del Proyecto

```
proyecto-final/
├── .github/
│   └── workflows/
│       └── ci.yml           # GitHub Actions
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models/
│   ├── schemas/
│   ├── repositories/
│   ├── services/
│   ├── routers/
│   ├── dependencies/
│   ├── exceptions/
│   └── utils/
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_*.py
├── alembic/                  # Migraciones
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── README.md
└── alembic.ini
```

---

## 🚀 Pasos Sugeridos

### Día 1-2: Setup y Modelos

1. Crear estructura de carpetas
2. Configurar Docker y docker-compose
3. Definir modelos SQLAlchemy
4. Configurar Alembic y crear migraciones
5. Crear schemas Pydantic

### Día 3-4: Autenticación y CRUD

1. Implementar registro y login
2. Configurar JWT
3. Crear dependencies de auth
4. Implementar CRUD de entidades
5. Agregar paginación

### Día 5: Testing

1. Configurar pytest
2. Crear fixtures en conftest.py
3. Tests de auth
4. Tests de CRUD
5. Verificar coverage

### Día 6: DevOps

1. Optimizar Dockerfile
2. Configurar GitHub Actions
3. Desplegar a producción
4. Probar en ambiente real

### Día 7: Documentación y Entrega

1. Completar README
2. Documentar endpoints
3. Preparar presentación
4. Revisar checklist final

---

## 📝 Entregables

1. **Repositorio GitHub** público con todo el código
2. **URL de producción** con la API desplegada
3. **Presentación** de 10-15 minutos

---

## 🎯 Criterios de Evaluación

| Criterio | Puntos | Descripción |
|----------|--------|-------------|
| Arquitectura | 20 | Estructura, separación de capas, código limpio |
| Auth | 20 | JWT completo, seguridad, roles |
| CRUD | 20 | Funcionalidad, validación, paginación |
| Testing | 15 | Cobertura, calidad de tests |
| DevOps | 15 | Docker, CI/CD, deployment |
| Documentación | 10 | README, OpenAPI, instrucciones |
| **Total** | **100** | |

**Bonus** (+10 pts máximo):
- Refresh tokens con blacklist (+3)
- Rate limiting (+2)
- Cache con Redis (+3)
- WebSockets (+2)

---

## 📚 Recursos

- [Semanas 1-4: Fundamentos](../week-01/)
- [Semanas 5-10: Backend Intermedio](../week-05/)
- [Semanas 11-14: Avanzado](../week-11/)
- [Semana 15: Docker y CI/CD](../week-15/)

---

## ❓ FAQ

**¿Puedo usar código de las prácticas?**
Sí, puedes reutilizar y adaptar código que escribiste durante el bootcamp.

**¿Qué plataforma de deployment usar?**
Railway, Render, o Fly.io tienen tiers gratuitos suficientes.

**¿El frontend es necesario?**
No, el foco es el backend. Un frontend básico es bonus.

**¿Puedo trabajar en equipo?**
El proyecto final es individual para la evaluación.

---

## 🏁 Checklist de Entrega

Antes de entregar, verifica:

- [ ] Código en GitHub público
- [ ] README con instrucciones claras
- [ ] Docker funciona localmente
- [ ] Tests pasan
- [ ] CI/CD configurado
- [ ] API desplegada y accesible
- [ ] Documentación OpenAPI completa
- [ ] Presentación preparada

---

¡Éxito en tu proyecto final! 🚀
