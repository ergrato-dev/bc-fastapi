# 🤖 Instrucciones para GitHub Copilot

## 📋 Contexto del Bootcamp

Este es un **Bootcamp de FastAPI Zero to Hero** estructurado para llevar a estudiantes de cero a héroe en desarrollo de APIs modernas con Python y FastAPI.

### 📊 Datos del Bootcamp

- **Duración**: 16 semanas (~4 meses)
- **Dedicación semanal**: 6 horas
- **Total de horas**: ~96 horas
- **Nivel de salida**: Desarrollador Backend Junior (FastAPI)
- **Enfoque**: FastAPI moderno con Python 3.13+
- **Stack**: FastAPI 0.115+, SQLAlchemy 2.x, Pydantic 2.10+, SQLite/PostgreSQL 17+, Docker 27+

---

## 🎯 Objetivos de Aprendizaje

Al finalizar el bootcamp, los estudiantes serán capaces de:

- ✅ Dominar los fundamentos de Python necesarios para desarrollo backend
- ✅ Construir APIs RESTful completas con FastAPI
- ✅ Implementar validación de datos robusta con Pydantic v2
- ✅ Trabajar con bases de datos usando SQLAlchemy (sync y async)
- ✅ Implementar autenticación y autorización (JWT, OAuth2)
- ✅ Escribir tests automatizados con pytest
- ✅ Documentar APIs automáticamente (OpenAPI/Swagger)
- ✅ Desplegar aplicaciones con Docker y servicios cloud
- ✅ Aplicar clean code, patrones de diseño y mejores prácticas
- ✅ Construir proyectos completos listos para producción

---

## 📚 Estructura del Bootcamp

### Distribución por Etapas

#### **Fundamentos (Semanas 1-4)** - 24 horas

- Introducción a Python moderno (3.12+)
- Type hints y tipado estático
- Programación asíncrona (async/await)
- Introducción a FastAPI y primeras APIs
- Pydantic v2: validación y serialización
- Rutas, parámetros y query strings

#### **Intermedio (Semanas 5-10)** - 36 horas

- Modelos de datos complejos con Pydantic
- SQLAlchemy ORM y Alembic (migraciones)
- Operaciones CRUD completas
- Relaciones entre modelos (1:N, N:M)
- Manejo de errores y excepciones personalizadas
- Middleware y dependencias
- Background tasks y eventos

#### **Avanzado (Semanas 11-14)** - 24 horas

- Autenticación JWT y OAuth2
- Autorización basada en roles (RBAC)
- Testing con pytest y pytest-asyncio
- WebSockets y Server-Sent Events
- Rate limiting y seguridad
- Logging y monitoreo

#### **Producción (Semanas 15-16)** - 12 horas

- Docker y containerización
- CI/CD básico (GitHub Actions)
- Deployment (Railway, Render, AWS)
- Proyecto final integrador
- Mejores prácticas de producción

---

## 🗂️ Estructura de Carpetas

Cada semana sigue esta estructura estándar:

```
bootcamp/week-XX/
├── README.md                 # Descripción y objetivos de la semana
├── rubrica-evaluacion.md     # Criterios de evaluación detallados
├── 0-assets/                 # Imágenes, diagramas y recursos visuales
├── 1-teoria/                 # Material teórico (archivos .md)
├── 2-practicas/              # Ejercicios guiados paso a paso
├── 3-proyecto/               # Proyecto semanal integrador con carpeta solution (oculta para el repo)
├── 4-recursos/               # Recursos adicionales
│   ├── ebooks-free/          # Libros electrónicos gratuitos
│   ├── videografia/          # Videos y tutoriales recomendados
│   └── webgrafia/            # Enlaces y documentación
└── 5-glosario/               # Términos clave de la semana (A-Z)
    └── README.md
```

### 📁 Carpetas Raíz

- **`_assets/`**: Recursos visuales globales (logos, headers, etc.)
- **`_docs/`**: Documentación general que aplica a todo el bootcamp
- **`_scripts/`**: Scripts de automatización y utilidades
- **`bootcamp/`**: Contenido semanal del bootcamp

---

## 🎓 Componentes de Cada Semana

### 1. **Teoría** (1-teoria/)

- Archivos markdown con explicaciones conceptuales
- Ejemplos de código con comentarios claros
- Diagramas y visualizaciones cuando sea necesario
- Referencias a documentación oficial de FastAPI

### 2. **Prácticas** (2-practicas/)

- Ejercicios guiados paso a paso
- Incremento progresivo de dificultad
- Soluciones comentadas
- Casos de uso del mundo real

#### 📋 Formato de Ejercicios

Los ejercicios son **tutoriales guiados**, NO tareas con TODOs. El estudiante aprende descomentando código:

**README.md del ejercicio:**

```markdown
### Paso 1: Crear endpoint GET básico

Explicación del concepto con ejemplo:

\`\`\`python
# Ejemplo explicativo
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
\`\`\`

**Abre `starter/main.py`** y descomenta la sección correspondiente.
```

**starter/main.py:**

```python
# ============================================
# PASO 1: Crear endpoint GET básico
# ============================================
print("--- Paso 1: Endpoint GET básico ---")

# Este endpoint recibe un parámetro de ruta
# Descomenta las siguientes líneas:
# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}

```

> ⚠️ **IMPORTANTE**: Los ejercicios NO tienen carpeta `solution/`. El estudiante aprende descomentando el código y verificando que funcione correctamente.

#### ❌ NO usar este formato en ejercicios:

```python
# ❌ INCORRECTO - Este formato es para PROYECTOS, no ejercicios
async def read_item(item_id: int):
    result = None  # TODO: Implementar
    return result
```

#### ✅ Usar este formato en ejercicios:

```python
# ✅ CORRECTO - Código comentado para descomentar
# Descomenta las siguientes líneas:
# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}
```

### 3. **Proyecto** (3-proyecto/)

- Proyecto integrador que consolida lo aprendido
- README.md con instrucciones claras
- Código inicial en `starter/`
- Carpeta `solution/` oculta (en `.gitignore`) solo para instructores
- Criterios de evaluación específicos

#### 📋 Formato de Proyecto (con TODOs)

A diferencia de los ejercicios, el proyecto SÍ usa TODOs para que el estudiante implemente desde cero:

**starter/main.py:**

```python
# ============================================
# FUNCIÓN: create_user
# Crea un nuevo usuario en la base de datos
# ============================================

from pydantic import BaseModel

class UserCreate(BaseModel):
    """Schema para crear usuario"""
    email: str
    password: str

async def create_user(user: UserCreate) -> dict:
    """
    Crea un nuevo usuario
    
    Args:
        user: Datos del usuario a crear
        
    Returns:
        dict: Usuario creado con su ID
    """
    # TODO: Implementar lógica de creación
    # 1. Validar que el email no exista
    # 2. Hashear la contraseña
    # 3. Guardar en base de datos
    # 4. Retornar usuario creado
    pass
```

El estudiante debe:

1. Leer las instrucciones en README.md
2. Completar cada TODO con su propia implementación
3. Usar lo aprendido en las prácticas guiadas

> 📁 **Estructura del proyecto:**
> ```
> 3-proyecto/
> ├── README.md          # Instrucciones del proyecto
> ├── starter/           # Código inicial para el estudiante
> └── solution/          # ⚠️ OCULTA - Solo para instructores
> ```
> 
> La carpeta `solution/` está en `.gitignore` y NO se sube al repositorio público.

### 4. **Recursos** (4-recursos/)

- **ebooks-free/**: Libros gratuitos relevantes
- **videografia/**: Videos tutoriales complementarios
- **webgrafia/**: Enlaces a documentación y artículos

### 5. **Glosario** (5-glosario/)

- Términos técnicos ordenados alfabéticamente
- Definiciones claras y concisas
- Ejemplos de código cuando aplique

---

## 📝 Convenciones de Código

### Estilo Python Moderno

```python
# ✅ BIEN - usar type hints siempre
def get_user(user_id: int) -> User | None:
    return db.query(User).filter(User.id == user_id).first()

# ✅ BIEN - usar async para operaciones I/O
async def fetch_data(url: str) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()

# ✅ BIEN - Pydantic para validación
class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)
    
    model_config = ConfigDict(str_strip_whitespace=True)

# ✅ BIEN - dependencias de FastAPI
async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
) -> User:
    return await verify_token(token, db)

# ❌ MAL - sin type hints
def get_user(user_id):
    return db.query(User).filter(User.id == user_id).first()

# ❌ MAL - usar sync cuando debería ser async
def fetch_data(url):
    response = requests.get(url)
    return response.json()
```

### Nomenclatura

- **Variables y funciones**: snake_case
- **Constantes globales**: UPPER_SNAKE_CASE
- **Clases**: PascalCase
- **Archivos**: snake_case.py
- **Endpoints**: kebab-case en URLs (`/user-profile`)
- **Idioma**: Inglés para código, español para documentación

### Estructura de Proyecto FastAPI

```
src/
├── main.py              # Punto de entrada
├── config.py            # Configuración
├── database.py          # Conexión a DB
├── models/              # Modelos SQLAlchemy
│   ├── __init__.py
│   └── user.py
├── schemas/             # Schemas Pydantic
│   ├── __init__.py
│   └── user.py
├── routers/             # Endpoints agrupados
│   ├── __init__.py
│   └── users.py
├── services/            # Lógica de negocio
│   ├── __init__.py
│   └── user_service.py
├── dependencies/        # Dependencias comunes
│   ├── __init__.py
│   └── auth.py
└── utils/               # Utilidades
    ├── __init__.py
    └── security.py
```

---

## 🧪 Testing

El bootcamp enseña testing con **pytest** y **pytest-asyncio**.

### Estructura de Tests

```python
# tests/test_users.py
import pytest
from httpx import AsyncClient
from src.main import app

@pytest.mark.asyncio
async def test_create_user():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post(
            "/users/",
            json={"email": "test@example.com", "password": "secret123"}
        )
        assert response.status_code == 201
        data = response.json()
        assert data["email"] == "test@example.com"
        assert "id" in data

@pytest.mark.asyncio
async def test_get_user_not_found():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/users/99999")
        assert response.status_code == 404
```

---

## 📖 Documentación

### README.md de Semana

Debe incluir:

1. **Título y descripción**
2. **🎯 Objetivos de aprendizaje**
3. **📚 Requisitos previos**
4. **🗂️ Estructura de la semana**
5. **📝 Contenidos** (con enlaces a teoría/prácticas)
6. **⏱️ Distribución del tiempo** (6 horas)
7. **📌 Entregables**
8. **🔗 Navegación** (anterior/siguiente semana)

### Archivos de Teoría

```markdown
# Título del Tema

## 🎯 Objetivos

- Objetivo 1
- Objetivo 2

## 📋 Contenido

### 1. Introducción

### 2. Conceptos Clave

### 3. Ejemplos Prácticos

### 4. Ejercicios

## 📚 Recursos Adicionales

## ✅ Checklist de Verificación
```

---

## 🎨 Recursos Visuales y Estándares de Diseño

### Formato de Assets

- ✅ **Preferir SVG** para todos los diagramas, iconos y gráficos
- ❌ **NO usar ASCII art** para diagramas o visualizaciones
- ✅ Usar PNG/JPG solo para screenshots o fotografías
- ✅ Optimizar imágenes antes de incluirlas

### Criterio para Assets SVG por Semana

Los assets SVG en `0-assets/` de cada semana tienen un propósito educativo específico:

- ✅ **Apoyo visual para comprensión de conceptos teóricos**
- ✅ **Diagramas de arquitectura** (flujo de datos, capas, etc.)
- ✅ **Visualización de procesos** (request/response, auth flow, etc.)
- ✅ **Headers de semana** para identificación visual

**Reglas de vinculación:**

1. Todo SVG debe estar **vinculado en al menos un archivo** de teoría o práctica
2. Usar sintaxis markdown: `![Descripción](../0-assets/nombre.svg)`
3. Incluir texto alternativo descriptivo para accesibilidad
4. Nombrar archivos descriptivamente: `async-flow.svg`, `http-methods.svg`

```markdown
<!-- Ejemplo de vinculación correcta en teoría -->
## Flujo Request/Response

![Diagrama del flujo HTTP request/response](../0-assets/http-flow.svg)

Como se observa en el diagrama, el cliente envía...
```

### Tema Visual

- 🌙 **Tema dark** para todos los assets visuales
- ❌ **Sin degradés** (gradients) en diseños
- ✅ Colores sólidos y contrastes claros
- ✅ Paleta consistente basada en verde FastAPI (#009688)

### Tipografía

- ✅ **Fuentes sans-serif** exclusivamente
- ✅ Recomendadas: Inter, Roboto, Open Sans, System UI
- ❌ **NO usar fuentes serif** (Times, Georgia, etc.)
- ✅ Mantener jerarquía visual clara

### Otros

- ✅ Incluir screenshots con anotaciones claras
- ✅ Mantener consistencia visual entre semanas
- ✅ Usar emojis para mejorar legibilidad (con moderación)

---

## 🌐 Idioma y Nomenclatura

### Código y Comentarios Técnicos

- ✅ **Nomenclatura en inglés** (variables, funciones, clases)
- ✅ **Comentarios de código en inglés**
- ✅ Usar términos técnicos estándar de la industria

```python
# ✅ CORRECTO - inglés
async def get_user_by_email(email: str) -> User | None:
    # Fetch user from database by email
    return await db.query(User).filter(User.email == email).first()

# ❌ INCORRECTO - español en código
async def obtener_usuario_por_email(correo: str) -> Usuario | None:
    # Obtener usuario de la base de datos por correo
    return await db.query(Usuario).filter(Usuario.correo == correo).first()
```

### Documentación

- ✅ **Documentación en español** (READMEs, teoría, guías)
- ✅ Explicaciones y tutoriales en español
- ✅ Comentarios educativos en español cuando expliquen conceptos

```python
# ✅ CORRECTO - código en inglés, explicación en español
async def calculate_discount(price: float, percentage: float) -> float:
    # En Python, los porcentajes se manejan como decimales
    # Por ejemplo: 20% = 0.20
    return price * (1 - percentage / 100)
```

---

## 🔐 Mejores Prácticas

### Código Limpio

- Nombres descriptivos y significativos
- Funciones pequeñas con una sola responsabilidad
- Comentarios solo cuando sea necesario explicar el "por qué"
- Evitar anidamiento profundo
- Usar early returns

### Seguridad

- Validar TODOS los inputs con Pydantic
- Usar hashing seguro para contraseñas (bcrypt/argon2)
- No exponer información sensible en errores
- Usar HTTPS en producción
- Implementar rate limiting
- Sanitizar queries SQL (usar ORM)

### Rendimiento

- Usar async/await para operaciones I/O
- Implementar paginación en listados
- Cachear respuestas cuando sea apropiado
- Usar connection pooling en bases de datos
- Lazy loading de relaciones

---

## 📊 Evaluación

Cada semana incluye **tres tipos de evidencias**:

1. **Conocimiento 🧠** (30%): Evaluaciones teóricas, cuestionarios
2. **Desempeño 💪** (40%): Ejercicios prácticos en clase
3. **Producto 📦** (30%): Proyecto entregable funcional

### Criterios de Aprobación

- Mínimo **70%** en cada tipo de evidencia
- Entrega puntual de proyectos
- Código funcional y bien documentado
- Tests pasando (cuando aplique)

---

## 🚀 Metodología de Aprendizaje

### Estrategias Didácticas

- **Aprendizaje Basado en Proyectos (ABP)**: Proyectos semanales integradores
- **Práctica Deliberada**: Ejercicios incrementales
- **API Challenges**: Problemas del mundo real
- **Code Review**: Revisión de código entre estudiantes
- **Live Coding**: Sesiones en vivo de programación

### Distribución del Tiempo (6h/semana)

- **Teoría**: 1.5-2 horas
- **Prácticas**: 2.5-3 horas
- **Proyecto**: 1.5-2 horas

---

## 🤖 Instrucciones para Copilot

Cuando trabajes en este proyecto:

### Límites de Respuesta

1. **Divide respuestas largas**

   - ❌ **NUNCA generar respuestas que superen los límites de tokens**
   - ✅ **SIEMPRE dividir contenido extenso en múltiples entregas**
   - ✅ Crear contenido por secciones, esperar confirmación del usuario
   - ✅ Priorizar calidad sobre cantidad en cada entrega
   - Razón: Evitar pérdida de contenido y garantizar completitud

2. **Estrategia de División**
   - Para semanas completas: dividir por carpetas (teoria → practicas → proyecto)
   - Para archivos grandes: dividir por secciones lógicas
   - Siempre indicar claramente qué parte se entrega y qué falta
   - Esperar confirmación del usuario antes de continuar

### Generación de Código

1. **Usa siempre sintaxis Python moderna (3.13+)**

   - Type hints obligatorios
   - Match statements cuando aplique
   - f-strings para formateo
   - Walrus operator cuando simplifique
   - Union types con `|` en lugar de `Union[]`
   - Genéricos nativos (`list[str]` en lugar de `List[str]`)

2. **Entorno de Desarrollo con Docker**

   - ✅ **USAR Docker** para evitar problemas con múltiples versiones de Python
   - ✅ **docker compose** para orquestar servicios (API, DB, etc.)
   - ✅ Crear archivos `.env` para configuración de entorno
   - Razón: Entorno consistente, reproducible y aislado para todos los estudiantes
   - Estructura recomendada:

     ```
     proyecto/
     ├── docker-compose.yml    # Orquestación de servicios
     ├── Dockerfile            # Imagen de la aplicación
     ├── .env.example          # Variables de entorno (template)
     ├── .env                  # Variables de entorno (ignorado en git)
     └── src/                  # Código fuente
     ```

   - Comandos esenciales:

     ```bash
     # Construir y levantar servicios
     docker compose up --build
     
     # Levantar en background
     docker compose up -d
     
     # Ver logs
     docker compose logs -f api
     
     # Ejecutar comandos dentro del contenedor
     docker compose exec api bash
     
     # Detener servicios
     docker compose down
     
     # Limpiar todo (incluye volúmenes)
     docker compose down -v
     ```

3. **Gestión de Paquetes (dentro de Docker)**

   - ❌ **NUNCA usar `pip`** directamente
   - ✅ **SOLO usar `uv`** como gestor de paquetes (rápido y moderno)
   - Razón: Mejor resolución de dependencias, compatibilidad con Docker
   - En Dockerfile:

     ```dockerfile
     FROM python:3.13-slim
     
     ENV PYTHONDONTWRITEBYTECODE=1 \
         PYTHONUNBUFFERED=1 \
         UV_SYSTEM_PYTHON=1
     
     RUN pip install --no-cache-dir uv
     
     WORKDIR /app
     COPY pyproject.toml uv.lock* ./
     RUN uv sync --frozen --no-dev
     
     COPY . .
     EXPOSE 8000
     CMD ["uv", "run", "fastapi", "dev", "src/main.py", "--host", "0.0.0.0", "--port", "8000"]
     ```

   - Comandos uv (dentro del contenedor):

     ```bash
     # Crear proyecto
     uv init
     
     # Instalar dependencias
     uv sync
     
     # Agregar paquete
     uv add fastapi
     
     # Agregar paquete de desarrollo
     uv add --dev pytest
     ```

4. **Base de Datos**

   - ✅ **SQLite** para desarrollo y **testing**
   - ✅ **PostgreSQL 16+** para producción
   - Razón: SQLite es perfecto para aprendizaje y tests (rápido, sin configuración)
   - **ORM**: SQLAlchemy 2.x (sync y async)
   - **Migraciones**: Alembic
   
   ```python
   # Configuración típica por entorno
   # .env.example
   DATABASE_URL=sqlite:///./app.db           # Desarrollo
   DATABASE_URL=sqlite:///:memory:           # Testing
   DATABASE_URL=postgresql://user:pass@db:5432/app  # Producción
   ```

5. **Documentación de API**

   - ✅ **OpenAPI/Swagger** (integrado en FastAPI)
   - Acceso automático en `/docs` (Swagger UI) y `/redoc` (ReDoc)
   - Documentar endpoints con docstrings y `response_model`
   
   ```python
   @app.get("/users/{user_id}", response_model=UserResponse)
   async def get_user(user_id: int) -> UserResponse:
       """
       Obtiene un usuario por su ID.
       
       - **user_id**: ID único del usuario
       """
       ...
   ```

6. **Comenta el código de manera educativa**

   - Explica conceptos para principiantes
   - Incluye referencias a documentación cuando sea útil
   - Usa comentarios que enseñen, no solo describan

6. **Proporciona ejemplos completos y funcionales**
   - Código que se pueda copiar y ejecutar
   - Incluye casos de uso realistas
   - Muestra tanto lo que se debe hacer como lo que se debe evitar

### Creación de Contenido

1. **Estructura clara y progresiva**

   - De lo simple a lo complejo
   - Conceptos construidos sobre conocimientos previos
   - Repetición espaciada de conceptos clave

2. **Ejemplos del mundo real**

   - Casos de uso prácticos y relevantes
   - Proyectos que los estudiantes puedan mostrar en portfolios
   - Problemas que encontrarán en el desarrollo real

3. **Enfoque moderno**
   - No mencionar características obsoletas
   - Enfocarse en mejores prácticas actuales
   - Usar herramientas y patrones modernos

### Respuestas y Ayuda

1. **Explicaciones claras**

   - Lenguaje simple y directo
   - Evitar jerga innecesaria
   - Proporcionar analogías cuando sea útil

2. **Código comentado**

   - Explicar cada paso importante
   - Destacar conceptos clave
   - Señalar posibles errores comunes

3. **Recursos adicionales**
   - Referencias a documentación oficial de FastAPI
   - Enlaces a Pydantic docs
   - Artículos relevantes de calidad

---

## 📚 Referencias Oficiales

- **FastAPI Documentation**: https://fastapi.tiangolo.com/
- **Pydantic Documentation**: https://docs.pydantic.dev/
- **SQLAlchemy Documentation**: https://docs.sqlalchemy.org/
- **Starlette Documentation**: https://www.starlette.io/
- **Python Documentation**: https://docs.python.org/3/
- **pytest Documentation**: https://docs.pytest.org/

---

## 🔗 Enlaces Importantes

- **Repositorio**: https://github.com/epti-dev/bc-fastapi
- **Documentación general**: [\_docs/README.md](_docs/README.md)
- **Primera semana**: [bootcamp/week-01/README.md](bootcamp/week-01/README.md)

---

## ✅ Checklist para Nuevas Semanas

Cuando crees contenido para una nueva semana:

- [ ] Crear estructura de carpetas completa
- [ ] README.md con objetivos y estructura
- [ ] Material teórico en 1-teoria/
- [ ] Ejercicios prácticos en 2-practicas/
- [ ] Proyecto integrador en 3-proyecto/
- [ ] Recursos adicionales en 4-recursos/
- [ ] Glosario de términos en 5-glosario/
- [ ] Rúbrica de evaluación
- [ ] Verificar coherencia con semanas anteriores
- [ ] Revisar progresión de dificultad
- [ ] Probar código de ejemplos

---

## 💡 Notas Finales

- **Prioridad**: Claridad sobre brevedad
- **Enfoque**: Aprendizaje práctico sobre teoría abstracta
- **Objetivo**: Preparar desarrolladores backend listos para trabajar
- **Filosofía**: FastAPI moderno desde el día 1

---

_Última actualización: Diciembre 2025_
_Versión: 1.0_
