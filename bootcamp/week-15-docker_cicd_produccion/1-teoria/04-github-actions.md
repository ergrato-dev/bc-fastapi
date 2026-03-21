# 🔄 GitHub Actions: CI/CD para FastAPI

## 🎯 Objetivos de Aprendizaje

- Entender qué es CI/CD y por qué es importante
- Crear workflows de GitHub Actions
- Configurar tests automatizados
- Implementar linting y type checking
- Construir y publicar imágenes Docker
- Gestionar secretos de forma segura

---

## 📋 Tabla de Contenidos

1. [¿Qué es CI/CD?](#qué-es-cicd)
2. [GitHub Actions Fundamentals](#github-actions-fundamentals)
3. [Estructura de un Workflow](#estructura-de-un-workflow)
4. [Workflows para FastAPI](#workflows-para-fastapi)
5. [Caché de Dependencias](#caché-de-dependencias)
6. [Secretos y Variables](#secretos-y-variables)
7. [Matrix Testing](#matrix-testing)
8. [Ejemplo Completo](#ejemplo-completo)

---

## ¿Qué es CI/CD?

![Pipeline CI/CD](../0-assets/04-cicd-pipeline.svg)

### CI - Continuous Integration

**Integración Continua**: Automatizar la verificación del código cada vez que se hace push.

```
Developer Push → Build → Test → Lint → ✅ Ready to merge
                                    → ❌ Fix issues
```

### CD - Continuous Delivery/Deployment

**Entrega Continua**: Automatizar el deployment a producción.

```
Merge to main → Build Image → Push to Registry → Deploy → ✅ Live
```

### Beneficios

| Sin CI/CD | Con CI/CD |
|-----------|-----------|
| Tests manuales (olvidables) | Tests automáticos siempre |
| "Funciona en mi máquina" | Funciona en entorno limpio |
| Deploy manual (propenso a errores) | Deploy automatizado |
| Feedback lento | Feedback en minutos |
| Bugs llegan a producción | Bugs detectados temprano |

---

## GitHub Actions Fundamentals

### Conceptos Clave

```
Workflow    → Proceso automatizado completo (archivo .yml)
    │
    ├── Event      → Trigger que inicia el workflow (push, PR, etc.)
    │
    └── Job        → Conjunto de steps que corren en un runner
            │
            ├── Runner  → Máquina virtual que ejecuta el job
            │
            └── Step    → Tarea individual (comando o action)
```

### Ejemplo Simple

```yaml
# .github/workflows/hello.yml
name: Hello World

on: push  # Event: se ejecuta en cada push

jobs:
  greet:  # Job name
    runs-on: ubuntu-latest  # Runner
    steps:
      - name: Say Hello  # Step
        run: echo "Hello, World!"
```

### Ubicación de Workflows

```
mi-proyecto/
├── .github/
│   └── workflows/
│       ├── ci.yml        # Tests y lint
│       ├── cd.yml        # Deploy
│       └── security.yml  # Escaneo de vulnerabilidades
└── src/
    └── ...
```

---

## Estructura de un Workflow

### Anatomía Completa

```yaml
# Nombre del workflow (aparece en UI de GitHub)
name: CI Pipeline

# Eventos que disparan el workflow
on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]
  workflow_dispatch:  # Permite ejecutar manualmente

# Variables de entorno globales
env:
  PYTHON_VERSION: "3.13"

# Jobs del workflow
jobs:
  # Primer job
  test:
    name: Run Tests
    runs-on: ubuntu-latest
    
    # Servicios (contenedores auxiliares)
    services:
      postgres:
        image: postgres:17
        env:
          POSTGRES_PASSWORD: test
        ports:
          - 5432:5432
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Run tests
        run: pytest
  
  # Segundo job (depende del primero)
  build:
    name: Build Image
    needs: test  # Espera a que test termine
    runs-on: ubuntu-latest
    steps:
      - run: docker build -t app .
```

### Events (Triggers)

```yaml
on:
  # Push a ramas específicas
  push:
    branches:
      - main
      - 'release/**'
    paths:
      - 'src/**'
      - 'tests/**'
    paths-ignore:
      - '**.md'
      - 'docs/**'
  
  # Pull requests
  pull_request:
    branches: [main]
    types: [opened, synchronize, reopened]
  
  # Scheduled (cron)
  schedule:
    - cron: '0 0 * * *'  # Diario a medianoche
  
  # Manual
  workflow_dispatch:
    inputs:
      environment:
        description: 'Deploy environment'
        required: true
        default: 'staging'
        type: choice
        options:
          - staging
          - production
  
  # Cuando otro workflow completa
  workflow_run:
    workflows: ["CI"]
    types: [completed]
```

### Runners

```yaml
jobs:
  build:
    # Runners de GitHub (gratuitos)
    runs-on: ubuntu-latest   # Ubuntu 22.04
    # runs-on: ubuntu-22.04  # Versión específica
    # runs-on: macos-latest  # macOS
    # runs-on: windows-latest # Windows
    
    # Self-hosted runner
    # runs-on: self-hosted
```

### Steps

```yaml
steps:
  # Usar una Action existente
  - name: Checkout
    uses: actions/checkout@v4
    with:
      fetch-depth: 0  # Parámetro de la action
  
  # Ejecutar comando shell
  - name: Install dependencies
    run: pip install -r requirements.txt
  
  # Múltiples comandos
  - name: Run tests
    run: |
      echo "Running tests..."
      pytest --cov
      echo "Done!"
  
  # Condicional
  - name: Deploy
    if: github.ref == 'refs/heads/main'
    run: ./deploy.sh
  
  # Con variables de entorno
  - name: Build
    env:
      NODE_ENV: production
    run: npm run build
```

---

## Workflows para FastAPI

### 1. Workflow de Tests

```yaml
# .github/workflows/test.yml
name: Tests

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    
    services:
      postgres:
        image: postgres:17-alpine
        env:
          POSTGRES_USER: test
          POSTGRES_PASSWORD: test
          POSTGRES_DB: test_db
        ports:
          - 5432:5432
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.13'
      
      - name: Install uv
        uses: astral-sh/setup-uv@v4
      
      - name: Install dependencies
        run: uv sync --frozen
      
      - name: Run tests
        env:
          DATABASE_URL: postgresql://test:test@localhost:5432/test_db
        run: uv run pytest --cov=src --cov-report=xml
      
      - name: Upload coverage
        uses: codecov/codecov-action@v4
        with:
          file: ./coverage.xml
```

### 2. Workflow de Lint

```yaml
# .github/workflows/lint.yml
name: Lint

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.13'
      
      - name: Install uv
        uses: astral-sh/setup-uv@v4
      
      - name: Install dependencies
        run: uv sync --frozen
      
      - name: Run ruff (linting)
        run: uv run ruff check src tests
      
      - name: Run ruff (formatting)
        run: uv run ruff format --check src tests
      
      - name: Run mypy (type checking)
        run: uv run mypy src
```

### 3. Workflow de Build Docker

```yaml
# .github/workflows/docker.yml
name: Docker Build

on:
  push:
    branches: [main]
    tags: ['v*']
  pull_request:
    branches: [main]

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3
      
      - name: Log in to Container Registry
        if: github.event_name != 'pull_request'
        uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      
      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          tags: |
            type=ref,event=branch
            type=ref,event=pr
            type=semver,pattern={{version}}
            type=sha
      
      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          context: .
          push: ${{ github.event_name != 'pull_request' }}
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
```

### 4. Workflow de Seguridad

```yaml
# .github/workflows/security.yml
name: Security Scan

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 0 * * 1'  # Lunes a medianoche

jobs:
  trivy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Build image
        run: docker build -t app:test .
      
      - name: Run Trivy vulnerability scanner
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: 'app:test'
          format: 'sarif'
          output: 'trivy-results.sarif'
          severity: 'CRITICAL,HIGH'
      
      - name: Upload Trivy scan results
        uses: github/codeql-action/upload-sarif@v3
        with:
          sarif_file: 'trivy-results.sarif'
  
  dependency-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.13'
      
      - name: Install safety
        run: pip install safety
      
      - name: Check dependencies
        run: safety check -r requirements.txt
```

---

## Caché de Dependencias

El caché acelera significativamente los workflows.

### Caché con uv

```yaml
- name: Install uv
  uses: astral-sh/setup-uv@v4
  with:
    enable-cache: true
    cache-dependency-glob: "uv.lock"

- name: Install dependencies
  run: uv sync --frozen
```

### Caché con pip

```yaml
- name: Set up Python
  uses: actions/setup-python@v5
  with:
    python-version: '3.13'
    cache: 'pip'
    cache-dependency-path: requirements.txt
```

### Caché Manual

```yaml
- name: Cache dependencies
  uses: actions/cache@v4
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}
    restore-keys: |
      ${{ runner.os }}-pip-
```

### Caché de Docker

```yaml
- name: Build and push
  uses: docker/build-push-action@v5
  with:
    context: .
    cache-from: type=gha
    cache-to: type=gha,mode=max
```

---

## Secretos y Variables

### Usar Secretos

```yaml
# Configurar en: Settings → Secrets → Actions

steps:
  - name: Deploy
    env:
      API_KEY: ${{ secrets.API_KEY }}
      DATABASE_URL: ${{ secrets.DATABASE_URL }}
    run: ./deploy.sh
```

### Variables de Entorno

```yaml
# Configurar en: Settings → Variables → Actions

env:
  APP_ENV: ${{ vars.APP_ENV }}

jobs:
  deploy:
    environment: production  # Usa variables de este environment
    steps:
      - run: echo "Deploying to ${{ vars.DEPLOY_URL }}"
```

### Secretos por Environment

```yaml
jobs:
  deploy-staging:
    environment: staging
    runs-on: ubuntu-latest
    steps:
      - run: ./deploy.sh
        env:
          API_KEY: ${{ secrets.API_KEY }}  # Secreto de staging
  
  deploy-production:
    environment: production
    needs: deploy-staging
    runs-on: ubuntu-latest
    steps:
      - run: ./deploy.sh
        env:
          API_KEY: ${{ secrets.API_KEY }}  # Secreto de production
```

### GITHUB_TOKEN

```yaml
# Token automático con permisos limitados
- name: Create Release
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
  run: gh release create v1.0.0

# Especificar permisos
permissions:
  contents: write
  packages: write
```

---

## Matrix Testing

Ejecutar tests en múltiples configuraciones.

### Matrix Simple

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.11', '3.12', '3.13']
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      
      - name: Test
        run: pytest
```

### Matrix Múltiple

```yaml
strategy:
  matrix:
    python-version: ['3.12', '3.13']
    os: [ubuntu-latest, macos-latest]
    database: [postgres, sqlite]
  fail-fast: false  # Continuar si uno falla
```

### Excluir/Incluir Combinaciones

```yaml
strategy:
  matrix:
    python-version: ['3.11', '3.12', '3.13']
    os: [ubuntu-latest, windows-latest]
    exclude:
      - os: windows-latest
        python-version: '3.11'
    include:
      - os: ubuntu-latest
        python-version: '3.13'
        experimental: true
```

---

## Ejemplo Completo

### Workflow CI Completo

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  PYTHON_VERSION: "3.13"

jobs:
  # =============================================
  # Job 1: Lint y Format
  # =============================================
  lint:
    name: Lint & Format
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Install uv
        uses: astral-sh/setup-uv@v4
        with:
          enable-cache: true
      
      - name: Set up Python
        run: uv python install ${{ env.PYTHON_VERSION }}
      
      - name: Install dependencies
        run: uv sync --frozen --group dev
      
      - name: Run ruff linter
        run: uv run ruff check src tests
      
      - name: Run ruff formatter
        run: uv run ruff format --check src tests
      
      - name: Run mypy
        run: uv run mypy src

  # =============================================
  # Job 2: Tests
  # =============================================
  test:
    name: Tests
    runs-on: ubuntu-latest
    
    services:
      postgres:
        image: postgres:17-alpine
        env:
          POSTGRES_USER: test
          POSTGRES_PASSWORD: test
          POSTGRES_DB: test_db
        ports:
          - 5432:5432
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
      
      redis:
        image: redis:7-alpine
        ports:
          - 6379:6379
        options: >-
          --health-cmd "redis-cli ping"
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Install uv
        uses: astral-sh/setup-uv@v4
        with:
          enable-cache: true
      
      - name: Set up Python
        run: uv python install ${{ env.PYTHON_VERSION }}
      
      - name: Install dependencies
        run: uv sync --frozen
      
      - name: Run tests with coverage
        env:
          DATABASE_URL: postgresql://test:test@localhost:5432/test_db
          REDIS_URL: redis://localhost:6379/0
          SECRET_KEY: test-secret-key
        run: |
          uv run pytest \
            --cov=src \
            --cov-report=xml \
            --cov-report=term-missing \
            -v
      
      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v4
        with:
          file: ./coverage.xml
          fail_ci_if_error: true

  # =============================================
  # Job 3: Build Docker
  # =============================================
  build:
    name: Build Docker Image
    runs-on: ubuntu-latest
    needs: [lint, test]
    
    permissions:
      contents: read
      packages: write
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3
      
      - name: Log in to GitHub Container Registry
        if: github.event_name != 'pull_request'
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      
      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ghcr.io/${{ github.repository }}
          tags: |
            type=ref,event=branch
            type=ref,event=pr
            type=sha,prefix=
      
      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          context: .
          push: ${{ github.event_name != 'pull_request' }}
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
      
      - name: Run Trivy vulnerability scanner
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: ghcr.io/${{ github.repository }}:${{ github.sha }}
          format: 'table'
          exit-code: '1'
          ignore-unfixed: true
          severity: 'CRITICAL,HIGH'
```

---

## 🧪 Verificación

```bash
# 1. Crear el workflow
mkdir -p .github/workflows
# Crear ci.yml con el contenido

# 2. Hacer push
git add .github/workflows/ci.yml
git commit -m "Add CI workflow"
git push

# 3. Ver en GitHub
# Actions tab → Ver ejecución del workflow

# 4. Crear PR para probar
git checkout -b test-ci
echo "# Test" >> README.md
git add . && git commit -m "Test CI"
git push -u origin test-ci
# Crear PR en GitHub
```

---

## 📚 Recursos Adicionales

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Workflow Syntax](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions)
- [Actions Marketplace](https://github.com/marketplace?type=actions)

---

## 🔗 Siguiente

Continúa con [05-deployment-cloud.md](05-deployment-cloud.md) para aprender a desplegar tu aplicación.
