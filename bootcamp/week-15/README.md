# 📦 Semana 15: Docker, CI/CD y Preparación para Producción

## 🎯 Objetivos de Aprendizaje

Al finalizar esta semana, serás capaz de:

- ✅ Crear imágenes Docker optimizadas para aplicaciones FastAPI
- ✅ Usar Docker Compose para orquestar múltiples servicios
- ✅ Implementar pipelines CI/CD con GitHub Actions
- ✅ Configurar tests automatizados, linting y security checks
- ✅ Preparar aplicaciones para deployment en servicios cloud
- ✅ Aplicar mejores prácticas de containerización

---

## 📋 Requisitos Previos

Antes de comenzar esta semana, deberías:

- ✅ Haber completado las semanas 1-14 del bootcamp
- ✅ Tener Docker Desktop instalado ([Bootcamp Docker](https://github.com/ergrato-dev/bc-docker))
- ✅ Tener una cuenta de GitHub
- ✅ Conocer los fundamentos de Git
- ✅ Haber trabajado con FastAPI, SQLAlchemy y testing

---

## 🗂️ Estructura de la Semana

```
week-15/
├── README.md                      # Este archivo
├── rubrica-evaluacion.md          # Criterios de evaluación
├── 0-assets/                      # Diagramas y recursos visuales
│   ├── 01-docker-architecture.svg
│   ├── 02-dockerfile-layers.svg
│   ├── 03-docker-compose-stack.svg
│   ├── 04-cicd-pipeline.svg
│   └── 05-deployment-options.svg
├── 1-teoria/                      # Material teórico
│   ├── 01-docker-fundamentos.md
│   ├── 02-dockerfile-optimizado.md
│   ├── 03-docker-compose.md
│   ├── 04-github-actions.md
│   └── 05-deployment-cloud.md
├── 2-practicas/                   # Ejercicios guiados
│   ├── 01-dockerfile-fastapi/
│   ├── 02-multi-stage-build/
│   ├── 03-docker-compose-stack/
│   └── 04-github-actions-cicd/
├── 3-proyecto/                    # Proyecto integrador
│   ├── README.md
│   └── starter/
├── 4-recursos/                    # Material complementario
│   ├── ebooks-free/
│   ├── videografia/
│   └── webgrafia/
└── 5-glosario/                    # Términos clave
    └── README.md
```

---

## 📚 Contenidos

### 1. Teoría

| Archivo | Tema | Duración |
|---------|------|----------|
| [01-docker-fundamentos.md](1-teoria/01-docker-fundamentos.md) | Conceptos de Docker, contenedores vs VMs | 25 min |
| [02-dockerfile-optimizado.md](1-teoria/02-dockerfile-optimizado.md) | Dockerfile, capas, multi-stage builds | 30 min |
| [03-docker-compose.md](1-teoria/03-docker-compose.md) | Orquestación, redes, volúmenes | 25 min |
| [04-github-actions.md](1-teoria/04-github-actions.md) | CI/CD, workflows, jobs, secrets | 30 min |
| [05-deployment-cloud.md](1-teoria/05-deployment-cloud.md) | Railway, Render, AWS opciones | 20 min |

### 2. Prácticas

| Ejercicio | Descripción | Duración |
|-----------|-------------|----------|
| [01-dockerfile-fastapi](2-practicas/01-dockerfile-fastapi/) | Crear Dockerfile para FastAPI | 30 min |
| [02-multi-stage-build](2-practicas/02-multi-stage-build/) | Optimizar imagen con multi-stage | 25 min |
| [03-docker-compose-stack](2-practicas/03-docker-compose-stack/) | API + DB + Redis con Compose | 35 min |
| [04-github-actions-cicd](2-practicas/04-github-actions-cicd/) | Pipeline completo CI/CD | 40 min |

### 3. Proyecto Integrador

| Proyecto | Descripción | Duración |
|----------|-------------|----------|
| [Task Manager Production-Ready](3-proyecto/) | Deploy completo con CI/CD | 60 min |

---

## ⏱️ Distribución del Tiempo

| Actividad | Tiempo |
|-----------|--------|
| 📖 Teoría | 2h 10min |
| 💻 Prácticas | 2h 10min |
| 🚀 Proyecto | 1h 00min |
| 📝 Evaluación | 40min |
| **Total** | **~6 horas** |

---

## 🔧 Stack Tecnológico

### Herramientas de Containerización

| Herramienta | Versión | Propósito |
|-------------|---------|-----------|
| Docker | 27+ | Containerización |
| Docker Compose | 2.x | Orquestación local |
| Docker Hub | - | Registry de imágenes |

### CI/CD

| Herramienta | Propósito |
|-------------|-----------|
| GitHub Actions | Pipelines automatizados |
| pytest | Tests automatizados |
| ruff | Linting Python |
| mypy | Type checking |
| trivy | Escaneo de vulnerabilidades |

### Deployment

| Servicio | Tipo | Complejidad |
|----------|------|-------------|
| Railway | PaaS | ⭐ Fácil |
| Render | PaaS | ⭐ Fácil |
| Fly.io | PaaS | ⭐⭐ Media |
| AWS ECS | IaaS | ⭐⭐⭐ Avanzado |

---

## 📌 Entregables

Al finalizar esta semana deberás entregar:

1. **Dockerfile optimizado** para tu API FastAPI
2. **docker-compose.yml** con stack completo (API + DB + Redis)
3. **Workflow de GitHub Actions** con tests, lint y build
4. **Documentación** de cómo hacer deploy
5. **Proyecto funcionando** en un servicio cloud (opcional)

---

## 🎯 Competencias a Desarrollar

### CE1: Containerización (25 pts)
- Crear Dockerfiles eficientes
- Optimizar tamaño de imágenes
- Usar multi-stage builds

### CE2: Orquestación (20 pts)
- Configurar Docker Compose
- Gestionar redes y volúmenes
- Variables de entorno

### CE3: CI/CD (25 pts)
- Crear workflows de GitHub Actions
- Configurar tests automatizados
- Implementar checks de calidad

### CE4: Deployment (20 pts)
- Preparar app para producción
- Configurar servicios cloud
- Gestionar secretos

### CE5: Mejores Prácticas (10 pts)
- Seguridad en contenedores
- Documentación
- .dockerignore apropiado

---

## 🔗 Navegación

| ← Anterior | Inicio | Siguiente → |
|------------|--------|-------------|
| [Semana 14: Rate Limiting, Seguridad, Logging](../week-14/README.md) | [Bootcamp](../README.md) | [Semana 16: Proyecto Final](../week-16/README.md) |

---

## 📖 Referencias Rápidas

- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Reference](https://docs.docker.com/compose/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Railway Docs](https://docs.railway.app/)
- [Render Docs](https://render.com/docs)

---

_Semana 15 de 16 · Etapa: Producción_
