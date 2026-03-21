# 🔄 Práctica 04: GitHub Actions CI/CD

## 🎯 Objetivo

Crear un pipeline CI/CD completo con GitHub Actions que ejecute tests, linting, y construya una imagen Docker.

---

## 📋 Conceptos que Aprenderás

- Estructura de workflows de GitHub Actions
- Jobs para tests, lint y build
- Configuración de servicios (PostgreSQL, Redis)
- Caché de dependencias
- Secretos y variables de entorno
- Build y push de imágenes Docker

---

## 🚀 Ejercicio

### Paso 1: Estructura del Workflow

```
.github/
└── workflows/
    └── ci.yml
```

Un workflow de GitHub Actions se compone de:
- **Triggers** (on): Cuándo se ejecuta
- **Jobs**: Tareas independientes
- **Steps**: Pasos dentro de cada job

### Paso 2: Crear el Workflow Básico

Abre `starter/.github/workflows/ci.yml` y descomenta paso a paso.

#### Header y Triggers

```yaml
name: CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]
```

- Se ejecuta en push a main/develop
- Se ejecuta en PRs hacia main

### Paso 3: Job de Lint

```yaml
jobs:
  lint:
    name: Lint & Format
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.13'
      
      - name: Install dependencies
        run: |
          pip install ruff mypy
          pip install -r requirements.txt
      
      - name: Run ruff
        run: ruff check src/
      
      - name: Run mypy
        run: mypy src/ --ignore-missing-imports
```

**Puntos clave:**
- `actions/checkout@v4` clona el repositorio
- `actions/setup-python@v5` instala Python
- `ruff` para linting/formatting
- `mypy` para type checking

### Paso 4: Job de Tests

```yaml
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
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.13'
          cache: 'pip'
      
      - name: Install dependencies
        run: pip install -r requirements.txt
      
      - name: Run tests
        env:
          DATABASE_URL: postgresql://test:test@localhost:5432/test_db
        run: pytest -v --cov=src
```

**Puntos clave:**
- `services` levanta contenedores auxiliares
- `healthcheck` espera a que PostgreSQL esté listo
- `cache: 'pip'` cachea dependencias
- Variables de entorno para tests

### Paso 5: Job de Build Docker

```yaml
  build:
    name: Build Docker
    runs-on: ubuntu-latest
    needs: [lint, test]  # Espera a que pasen lint y test
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3
      
      - name: Build image
        uses: docker/build-push-action@v5
        with:
          context: .
          push: false
          tags: myapp:${{ github.sha }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
```

**Puntos clave:**
- `needs: [lint, test]` crea dependencia entre jobs
- `docker/setup-buildx-action` configura Buildx
- `cache-from/to: type=gha` usa caché de GitHub Actions

### Paso 6: Probar Localmente (act)

Puedes probar workflows localmente con `act`:

```bash
# Instalar act (si no lo tienes)
# macOS: brew install act
# Linux: curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash

# Ejecutar workflow
act -j lint
act -j test
```

### Paso 7: Configurar en GitHub

1. Crear repositorio en GitHub
2. Push del código:
   ```bash
   git init
   git add .
   git commit -m "Initial commit with CI"
   git remote add origin https://github.com/tu-usuario/tu-repo.git
   git push -u origin main
   ```
3. Ir a Actions tab en GitHub
4. Ver la ejecución del workflow

---

## 🧪 Verificación

El workflow debe:
- ✅ Ejecutarse en cada push
- ✅ Lint job pasa sin errores
- ✅ Test job ejecuta tests exitosamente
- ✅ Build job construye imagen Docker

---

## 📝 Workflow Completo

```yaml
name: CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  lint:
    name: Lint & Format
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.13'
      
      - name: Install linters
        run: pip install ruff mypy
      
      - name: Install dependencies
        run: pip install -r requirements.txt
      
      - name: Run ruff check
        run: ruff check src/
      
      - name: Run ruff format check
        run: ruff format --check src/
      
      - name: Run mypy
        run: mypy src/ --ignore-missing-imports

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
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.13'
          cache: 'pip'
      
      - name: Install dependencies
        run: pip install -r requirements.txt
      
      - name: Run tests with coverage
        env:
          DATABASE_URL: postgresql://test:test@localhost:5432/test_db
          SECRET_KEY: test-secret-key
        run: pytest -v --cov=src --cov-report=xml
      
      - name: Upload coverage
        uses: codecov/codecov-action@v4
        with:
          file: ./coverage.xml

  build:
    name: Build Docker
    runs-on: ubuntu-latest
    needs: [lint, test]
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3
      
      - name: Build image
        uses: docker/build-push-action@v5
        with:
          context: .
          push: false
          tags: myapp:${{ github.sha }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
```

---

## 🎯 Desafío Extra

1. Agrega un job que haga push de la imagen a GitHub Container Registry
2. Agrega matrix testing para Python 3.12 y 3.13
3. Agrega escaneo de vulnerabilidades con Trivy
4. Configura notificaciones a Slack/Discord

---

## 📚 Recursos

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Actions Marketplace](https://github.com/marketplace?type=actions)
- [act - Run GitHub Actions locally](https://github.com/nektos/act)

---

## 🔗 Siguiente

Has completado las prácticas de la Semana 15. Continúa con el [Proyecto Integrador](../../3-proyecto/).
