# 🚀 Deployment: Desplegando FastAPI en la Nube

## 🎯 Objetivos de Aprendizaje

- Conocer las opciones de deployment para aplicaciones FastAPI
- Preparar una aplicación para producción
- Desplegar en Railway, Render y otras plataformas
- Configurar bases de datos en producción
- Gestionar variables de entorno y secretos

---

## 📋 Tabla de Contenidos

1. [Preparación para Producción](#preparación-para-producción)
2. [Opciones de Deployment](#opciones-de-deployment)
3. [Railway](#railway)
4. [Render](#render)
5. [Fly.io](#flyio)
6. [AWS (Introducción)](#aws-introducción)
7. [Checklist de Producción](#checklist-de-producción)

---

## Preparación para Producción

![Opciones de Deployment](../0-assets/05-deployment-options.svg)

### Diferencias Dev vs Prod

| Aspecto | Desarrollo | Producción |
|---------|------------|------------|
| Debug | Activado | **Desactivado** |
| Reload | Hot reload | **Sin reload** |
| Workers | 1 | **Múltiples (CPU cores)** |
| Database | SQLite local | **PostgreSQL managed** |
| Logs | Console, verbose | **Structured JSON** |
| Secrets | .env local | **Variables de entorno** |
| HTTPS | No | **Sí (obligatorio)** |

### Configuración por Entorno

```python
# src/config.py
from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    # Application
    app_name: str = "FastAPI App"
    debug: bool = False
    environment: str = "production"
    
    # Server
    host: str = "0.0.0.0"
    port: int = 8000
    workers: int = 4
    
    # Database
    database_url: str
    
    # Security
    secret_key: str
    allowed_hosts: list[str] = ["*"]
    cors_origins: list[str] = []
    
    # Optional services
    redis_url: str | None = None
    sentry_dsn: str | None = None
    
    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "extra": "ignore",
    }


@lru_cache
def get_settings() -> Settings:
    return Settings()
```

### Dockerfile de Producción

```dockerfile
# Dockerfile
FROM python:3.13-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN pip install --no-cache-dir uv

WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

# Runtime stage
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH"

WORKDIR /app

# Non-root user
RUN adduser --disabled-password --gecos "" --uid 1000 appuser

# Copy virtualenv and code
COPY --from=builder /app/.venv ./.venv
COPY src/ ./src/
COPY alembic/ ./alembic/
COPY alembic.ini ./

# Change ownership
RUN chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

# Production command with multiple workers
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
```

### Variables de Entorno Requeridas

```bash
# .env.example (documentación)

# ========================================
# REQUIRED - Application will not start without these
# ========================================

# Database connection string
# Format: postgresql://USER:PASSWORD@HOST:PORT/DATABASE
DATABASE_URL=postgresql://user:password@localhost:5432/dbname

# Secret key for JWT tokens (generate with: openssl rand -hex 32)
SECRET_KEY=your-secret-key-here

# ========================================
# OPTIONAL - Defaults provided
# ========================================

# Environment: development, staging, production
ENVIRONMENT=production

# Debug mode (never true in production!)
DEBUG=false

# Server configuration
HOST=0.0.0.0
PORT=8000
WORKERS=4

# CORS origins (comma-separated)
CORS_ORIGINS=https://myapp.com,https://www.myapp.com

# Redis for caching/sessions (optional)
REDIS_URL=redis://localhost:6379/0

# Error tracking (optional)
SENTRY_DSN=https://xxx@sentry.io/xxx
```

---

## Opciones de Deployment

### Comparativa de Plataformas

| Plataforma | Tipo | Free Tier | Complejidad | PostgreSQL |
|------------|------|-----------|-------------|------------|
| **Railway** | PaaS | $5/mes crédito | ⭐ Fácil | ✅ Incluido |
| **Render** | PaaS | Limitado | ⭐ Fácil | ✅ Incluido |
| **Fly.io** | PaaS | Generoso | ⭐⭐ Media | ✅ Incluido |
| **Vercel** | Serverless | Generoso | ⭐ Fácil | ❌ Externo |
| **AWS ECS** | IaaS | Free tier | ⭐⭐⭐ Alta | ✅ RDS |
| **Google Cloud Run** | Serverless | Generoso | ⭐⭐ Media | ✅ Cloud SQL |
| **DigitalOcean App** | PaaS | No | ⭐⭐ Media | ✅ Incluido |

### Recomendación por Caso de Uso

```
Proyecto personal / MVP:
  → Railway o Render (más simple)

Startup early-stage:
  → Fly.io (mejor precio/rendimiento)

Empresa establecida:
  → AWS / GCP / Azure (más control)

Solo API (sin DB compleja):
  → Vercel / Cloud Run (serverless)
```

---

## Railway

[Railway](https://railway.app) es una plataforma PaaS moderna, excelente para FastAPI.

### Características

- ✅ Deploy desde GitHub automático
- ✅ PostgreSQL y Redis incluidos
- ✅ Variables de entorno fáciles
- ✅ Logs en tiempo real
- ✅ $5/mes de crédito gratis
- ✅ Dominio automático (.up.railway.app)

### Deploy con Railway

#### 1. Preparar el Proyecto

```bash
# Estructura necesaria
my-project/
├── Dockerfile          # Railway lo detecta automáticamente
├── pyproject.toml
├── uv.lock
└── src/
    └── main.py
```

#### 2. Archivo railway.toml (opcional)

```toml
# railway.toml
[build]
builder = "dockerfile"
dockerfilePath = "Dockerfile"

[deploy]
healthcheckPath = "/health"
healthcheckTimeout = 100
restartPolicyType = "on_failure"
restartPolicyMaxRetries = 3
```

#### 3. Deploy

```bash
# Opción 1: CLI
npm install -g @railway/cli
railway login
railway init
railway up

# Opción 2: GitHub (recomendado)
# 1. Conectar repo en railway.app
# 2. Railway detecta Dockerfile
# 3. Deploy automático en cada push
```

#### 4. Agregar PostgreSQL

```bash
# En Railway Dashboard:
# 1. New → Database → PostgreSQL
# 2. Railway crea DATABASE_URL automáticamente
# 3. Tu app puede usar $DATABASE_URL
```

#### 5. Variables de Entorno

```bash
# En Railway Dashboard → Variables
SECRET_KEY=xxx
ENVIRONMENT=production
DEBUG=false

# O via CLI
railway variables set SECRET_KEY=xxx
```

### Ejemplo de Workflow para Railway

```yaml
# .github/workflows/deploy-railway.yml
name: Deploy to Railway

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Install Railway CLI
        run: npm install -g @railway/cli
      
      - name: Deploy
        env:
          RAILWAY_TOKEN: ${{ secrets.RAILWAY_TOKEN }}
        run: railway up --detach
```

---

## Render

[Render](https://render.com) es otra excelente opción PaaS con un free tier.

### Características

- ✅ Free tier (con limitaciones)
- ✅ PostgreSQL managed
- ✅ Deploy desde GitHub
- ✅ Auto-scaling disponible
- ⚠️ Free tier duerme después de 15 min inactividad

### Deploy con Render

#### 1. Archivo render.yaml

```yaml
# render.yaml
services:
  - type: web
    name: fastapi-app
    env: docker
    dockerfilePath: ./Dockerfile
    dockerContext: .
    healthCheckPath: /health
    envVars:
      - key: DATABASE_URL
        fromDatabase:
          name: fastapi-db
          property: connectionString
      - key: SECRET_KEY
        generateValue: true
      - key: ENVIRONMENT
        value: production

databases:
  - name: fastapi-db
    databaseName: appdb
    user: appuser
    plan: free  # o starter, standard, etc.
```

#### 2. Deploy Manual

1. Ir a [render.com](https://render.com)
2. New → Web Service
3. Conectar repositorio GitHub
4. Seleccionar "Docker"
5. Configurar variables de entorno
6. Deploy

#### 3. Configurar Base de Datos

```bash
# Render crea automáticamente la variable DATABASE_URL
# En formato: postgresql://user:pass@host/dbname

# Para conectarte localmente (debugging):
# Dashboard → Database → External Connection String
```

---

## Fly.io

[Fly.io](https://fly.io) ofrece excelente rendimiento y un free tier generoso.

### Características

- ✅ Free tier: 3 VMs pequeñas
- ✅ Edge deployment (múltiples regiones)
- ✅ PostgreSQL y Redis
- ✅ Muy buen rendimiento
- ⭐⭐ Requiere algo más de configuración

### Deploy con Fly.io

#### 1. Instalar CLI

```bash
# macOS
brew install flyctl

# Linux
curl -L https://fly.io/install.sh | sh

# Login
fly auth login
```

#### 2. Crear App

```bash
fly launch
# Responder preguntas interactivas
# - App name
# - Region
# - PostgreSQL (si/no)
# - Redis (si/no)
```

#### 3. Archivo fly.toml

```toml
# fly.toml
app = "my-fastapi-app"
primary_region = "mia"  # Miami

[build]
  dockerfile = "Dockerfile"

[env]
  ENVIRONMENT = "production"
  PORT = "8000"

[http_service]
  internal_port = 8000
  force_https = true
  auto_stop_machines = true
  auto_start_machines = true
  min_machines_running = 1

  [http_service.concurrency]
    type = "connections"
    hard_limit = 100
    soft_limit = 80

[[vm]]
  cpu_kind = "shared"
  cpus = 1
  memory_mb = 256
```

#### 4. Secretos

```bash
# Configurar secretos (no van en fly.toml)
fly secrets set SECRET_KEY=xxx
fly secrets set DATABASE_URL=xxx

# Ver secretos configurados
fly secrets list
```

#### 5. Deploy

```bash
# Deploy manual
fly deploy

# Ver logs
fly logs

# Ver status
fly status

# Conectar a la app
fly ssh console
```

#### 6. Base de Datos

```bash
# Crear PostgreSQL
fly postgres create

# Attach a tu app
fly postgres attach my-postgres-db

# Fly configura DATABASE_URL automáticamente
```

---

## AWS (Introducción)

AWS ofrece más control pero mayor complejidad. Aquí una introducción básica.

### Opciones en AWS

```
Simple → Complejo

1. AWS App Runner
   - Similar a Railway/Render
   - Detecta Dockerfile
   - Managed, fácil de usar

2. AWS Elastic Beanstalk
   - PaaS tradicional
   - Más configuración
   - Más control

3. AWS ECS (Fargate)
   - Contenedores serverless
   - Alta configuración
   - Muy flexible

4. AWS ECS (EC2)
   - Contenedores en EC2
   - Máximo control
   - Requiere gestionar infraestructura

5. AWS EKS
   - Kubernetes managed
   - Para equipos con experiencia K8s
   - Máxima complejidad
```

### AWS App Runner (Más Simple)

```bash
# 1. Crear servicio desde consola AWS
# 2. Conectar repositorio GitHub
# 3. Configurar:
#    - Port: 8000
#    - Health check: /health
#    - Variables de entorno

# O usar CLI
aws apprunner create-service \
  --service-name my-fastapi \
  --source-configuration '{
    "CodeRepository": {
      "RepositoryUrl": "https://github.com/user/repo",
      "SourceCodeVersion": {"Type": "BRANCH", "Value": "main"},
      "CodeConfiguration": {
        "ConfigurationSource": "REPOSITORY"
      }
    }
  }'
```

### RDS para Base de Datos

```bash
# Crear PostgreSQL en RDS
aws rds create-db-instance \
  --db-instance-identifier my-postgres \
  --db-instance-class db.t3.micro \
  --engine postgres \
  --master-username admin \
  --master-user-password xxx \
  --allocated-storage 20

# Obtener endpoint
aws rds describe-db-instances \
  --db-instance-identifier my-postgres \
  --query 'DBInstances[0].Endpoint'
```

---

## Checklist de Producción

### Pre-Deploy

```markdown
## Código
- [ ] Tests pasan al 100%
- [ ] Linting sin errores
- [ ] Type checking sin errores
- [ ] Sin código de debug (print, pdb, etc.)
- [ ] Sin secretos en código

## Configuración
- [ ] Variables de entorno documentadas
- [ ] .env.example actualizado
- [ ] Configuración por entorno (dev/staging/prod)
- [ ] DEBUG=false en producción
- [ ] SECRET_KEY generado de forma segura

## Base de Datos
- [ ] Migraciones probadas
- [ ] Backup configurado
- [ ] Connection pooling
- [ ] Índices necesarios creados

## Seguridad
- [ ] HTTPS obligatorio
- [ ] CORS configurado correctamente
- [ ] Rate limiting activo
- [ ] Headers de seguridad
- [ ] Dependencias actualizadas

## Observabilidad
- [ ] Health check endpoint
- [ ] Logging estructurado
- [ ] Métricas básicas
- [ ] Error tracking (Sentry)
```

### Post-Deploy

```markdown
## Verificación
- [ ] App responde en URL de producción
- [ ] Health check pasa
- [ ] Endpoints principales funcionan
- [ ] Base de datos conecta correctamente
- [ ] Logs visibles y estructurados

## Monitoreo
- [ ] Alertas configuradas
- [ ] Dashboard de métricas
- [ ] Notificaciones de errores

## Documentación
- [ ] README actualizado
- [ ] Proceso de deploy documentado
- [ ] Runbook para incidentes
- [ ] Contactos de emergencia
```

### Script de Verificación

```python
# scripts/verify_deployment.py
import httpx
import sys

BASE_URL = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8000"

def check_health():
    """Verify health endpoint."""
    response = httpx.get(f"{BASE_URL}/health", timeout=10)
    assert response.status_code == 200
    data = response.json()
    assert data.get("status") == "healthy"
    print("✅ Health check passed")

def check_docs():
    """Verify OpenAPI docs are available."""
    response = httpx.get(f"{BASE_URL}/docs", timeout=10)
    assert response.status_code == 200
    print("✅ Docs available")

def check_api():
    """Verify main API endpoint."""
    response = httpx.get(f"{BASE_URL}/api/v1/", timeout=10)
    assert response.status_code in [200, 404]  # 404 is ok if no root endpoint
    print("✅ API responding")

if __name__ == "__main__":
    try:
        check_health()
        check_docs()
        check_api()
        print(f"\n🎉 All checks passed for {BASE_URL}")
    except Exception as e:
        print(f"\n❌ Verification failed: {e}")
        sys.exit(1)
```

```bash
# Uso
python scripts/verify_deployment.py https://my-app.railway.app
```

---

## 🧪 Ejercicio Práctico

Despliega tu aplicación FastAPI en Railway:

1. Crear cuenta en [railway.app](https://railway.app)
2. Conectar tu repositorio de GitHub
3. Agregar PostgreSQL
4. Configurar variables de entorno
5. Verificar deploy con el script anterior

---

## 📚 Recursos Adicionales

- [Railway Documentation](https://docs.railway.app/)
- [Render Documentation](https://render.com/docs)
- [Fly.io Documentation](https://fly.io/docs/)
- [AWS App Runner](https://aws.amazon.com/apprunner/)

---

## 🔗 Siguiente

Has completado la teoría de la Semana 15. Ahora practica con los [ejercicios guiados](../2-practicas/).
