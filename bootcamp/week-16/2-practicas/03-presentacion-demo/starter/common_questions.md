# ❓ Preguntas Frecuentes en Presentaciones

Prepara respuestas para estas preguntas comunes. El evaluador probablemente hará 2-3 de estas.

---

## 🏗️ Arquitectura

### ¿Por qué elegiste FastAPI?
```
Elegí FastAPI porque:
1. Es muy rápido gracias a ASGI y Starlette
2. Tiene validación automática con Pydantic
3. Genera documentación OpenAPI automáticamente
4. Tiene excelente soporte para async/await
5. Es moderno y tiene una comunidad activa

Comparado con Flask o Django REST:
- Flask es más simple pero requiere más configuración manual
- Django REST es más completo pero más pesado
- FastAPI está en el punto medio: productivo y performante
```

### ¿Cómo estructuraste el proyecto?
```
Usé una arquitectura en capas:

1. Routers: Reciben requests, validan con Pydantic, llaman a services
2. Services: Contienen la lógica de negocio
3. Repositories: Encapsulan acceso a base de datos
4. Models: Definiciones de SQLAlchemy
5. Schemas: Validación de entrada/salida con Pydantic

Beneficios:
- Cada capa tiene una responsabilidad clara
- Fácil de testear (puedo mockear repositories)
- Fácil de mantener y extender
```

### ¿Por qué usaste PostgreSQL?
```
PostgreSQL porque:
1. Es robusto y probado en producción
2. Soporte completo de ACID (transacciones)
3. Buen rendimiento con índices
4. JSON nativo si necesito flexibilidad
5. Es el estándar en la industria

Para desarrollo uso SQLite por simplicidad,
pero el código es agnóstico gracias a SQLAlchemy.
```

---

## 🔐 Seguridad

### ¿Cómo funciona tu autenticación?
```
Implementé JWT (JSON Web Tokens):

1. Usuario envía email/password a /login
2. Valido credenciales contra hash en DB (bcrypt)
3. Si es válido, genero access token (15 min) y refresh token (7 días)
4. Cliente envía access token en header Authorization
5. Cada request valida firma y expiración del token

Refresh token:
- Permite renovar access token sin re-login
- Almacenado de forma segura en el cliente
- Se puede revocar si hay compromiso de seguridad
```

### ¿Cómo manejas la autorización?
```
Tengo dos niveles:

1. Autenticación: ¿Quién eres? (JWT válido)
2. Autorización: ¿Qué puedes hacer? (roles y ownership)

Implementé:
- Roles: admin, user
- Ownership: usuarios solo ven/editan sus propios recursos
- Dependency de FastAPI verifica permisos antes de ejecutar

Ejemplo:
- GET /tasks → Solo tareas del usuario autenticado
- DELETE /users/{id} → Solo admin
```

### ¿Cómo proteges contra ataques comunes?
```
Implementé protección contra:

1. SQL Injection: Uso ORM, nunca string formatting en queries
2. Password débiles: Validación de complejidad con Pydantic
3. Brute force: Rate limiting (X requests por minuto)
4. XSS: Pydantic escapa strings automáticamente
5. CORS: Configurado solo para dominios permitidos

También:
- Secrets en variables de entorno, nunca en código
- HTTPS obligatorio en producción
- Headers de seguridad configurados
```

---

## 🧪 Testing

### ¿Cómo testeaste la aplicación?
```
Usé pytest con varios niveles:

1. Unit tests: Funciones y servicios aislados
2. Integration tests: Endpoints con DB de prueba
3. Fixtures: Datos de prueba reutilizables

Herramientas:
- pytest-asyncio para tests async
- httpx.AsyncClient para test de endpoints
- SQLite en memoria para tests rápidos

Coverage: [X]% (mostrar número real)
```

### ¿Qué harías para mejorar el testing?
```
Con más tiempo agregaría:

1. Tests de contrato (contract testing) para API
2. Tests de carga con locust o k6
3. Tests E2E si hubiera frontend
4. Mutation testing para validar calidad de tests
5. Tests de seguridad automatizados (OWASP ZAP)
```

---

## ⚡ Rendimiento

### ¿Cómo optimizaste el rendimiento?
```
Varias técnicas:

1. Async/await: No bloqueo en operaciones I/O
2. Connection pooling: Reutilizo conexiones a DB
3. Eager loading: Evito N+1 queries con selectinload
4. Paginación: No cargo miles de registros
5. Índices: En campos de búsqueda frecuente

Si tuviera más tiempo:
- Agregaría Redis para cache
- Implementaría compresión gzip
- Optimizaría queries más pesadas
```

### ¿Qué pasa si hay miles de usuarios?
```
El sistema escala porque:

1. FastAPI es async, maneja muchas conexiones concurrentes
2. PostgreSQL puede manejar miles de conexiones con pgbouncer
3. Docker permite escalar horizontalmente
4. Paginación previene queries masivas

Para escalar más:
- Load balancer con múltiples instancias
- Cache distribuido (Redis cluster)
- Read replicas para queries pesadas
- CDN para assets estáticos
```

---

## 🐳 DevOps

### ¿Por qué Docker?
```
Docker me da:

1. Consistencia: Mismo ambiente en dev y producción
2. Aislamiento: Dependencias no chocan entre proyectos
3. Facilidad de deploy: Un comando levanta todo
4. Escalabilidad: Fácil replicar contenedores

Mi setup:
- Dockerfile multi-stage (imagen pequeña y segura)
- docker-compose para orquestar API + DB
- Usuario no-root por seguridad
```

### ¿Cómo funciona tu CI/CD?
```
GitHub Actions ejecuta en cada push:

1. Lint (Ruff): Verifica estilo de código
2. Type check (Pyright): Verifica tipos
3. Tests (pytest): Ejecuta suite de tests
4. Build (Docker): Construye imagen
5. Deploy: Si es main, despliega a producción

Beneficios:
- Detecta errores antes de merge
- Deploy automático reduce errores humanos
- Historial de builds para debugging
```

---

## 💡 Decisiones Técnicas

### ¿Qué fue lo más difícil?
```
[Sé honesto - comparte un desafío real]

Ejemplo:
"Lo más difícil fue implementar el refresh token correctamente.
Al principio no invalidaba tokens viejos y tuve que agregar
una lista negra. Aprendí sobre la diferencia entre stateless
y stateful auth."
```

### ¿Qué harías diferente si empezaras de nuevo?
```
[Muestra reflexión y aprendizaje]

Ejemplo:
"Empezaría con tests desde el día uno.
Agregué tests al final y encontré bugs que hubiera
detectado antes. También usaría migraciones desde
el inicio en lugar de recrear la DB."
```

### ¿Cómo manejas los errores?
```
Implementé manejo centralizado:

1. Excepciones personalizadas por tipo de error
2. Exception handler global en FastAPI
3. Formato consistente de respuesta:
   {"detail": "mensaje", "code": "ERROR_CODE"}
4. Logging de errores para debugging
5. Errores no exponen info sensible al cliente
```

---

## 📝 Template de Respuesta

Cuando no sepas la respuesta exacta:

```
"No implementé eso específicamente, pero el approach sería:
[describe cómo lo resolverías]

Por ejemplo, para [problema] usaría [solución]
porque [razón técnica]."
```

```
"Esa es una buena pregunta. En mi implementación actual
[describe lo que hiciste]. Si necesitara [lo que preguntaron],
consideraría [opción 1] o [opción 2]."
```

---

## 🎯 Practica

1. Lee cada pregunta en voz alta
2. Responde sin mirar la respuesta sugerida
3. Compara con la guía
4. Repite hasta que fluya naturalmente
