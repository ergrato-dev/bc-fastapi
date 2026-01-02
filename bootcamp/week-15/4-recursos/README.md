# 📚 Recursos Adicionales - Semana 15

## 🎥 Videografía Recomendada

### Docker Fundamentals

| Video | Canal | Duración | Enlace |
|-------|-------|----------|--------|
| Docker Tutorial for Beginners | TechWorld with Nana | 2h 46m | [YouTube](https://www.youtube.com/watch?v=3c-iBn73dDE) |
| Docker Compose Tutorial | NetworkChuck | 30m | [YouTube](https://www.youtube.com/watch?v=DM65_JyGxCo) |
| Multi-stage Docker Builds | Docker | 15m | [YouTube](https://www.youtube.com/watch?v=zpkqNPwEzac) |

### GitHub Actions

| Video | Canal | Duración | Enlace |
|-------|-------|----------|--------|
| GitHub Actions Tutorial | TechWorld with Nana | 1h | [YouTube](https://www.youtube.com/watch?v=R8_veQiYBjI) |
| CI/CD Pipeline with GitHub Actions | Fireship | 12m | [YouTube](https://www.youtube.com/watch?v=eB0nUzAI7M8) |
| GitHub Actions for Python | ArjanCodes | 20m | [YouTube](https://www.youtube.com/watch?v=WTofttoD2xg) |

### FastAPI + Docker

| Video | Canal | Duración | Enlace |
|-------|-------|----------|--------|
| FastAPI with Docker | Patrick Loeber | 25m | [YouTube](https://www.youtube.com/watch?v=bi0cKgmRuiA) |
| Deploying FastAPI to Production | JetBrains | 45m | [YouTube](https://www.youtube.com/watch?v=XjNGVMxYbPk) |

---

## 🔗 Webgrafía

### Documentación Oficial

- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Specification](https://docs.docker.com/compose/compose-file/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [FastAPI Deployment Guide](https://fastapi.tiangolo.com/deployment/)

### Best Practices

- [Dockerfile Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [Docker Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html)
- [GitHub Actions Best Practices](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)

### Herramientas

- [Dive - Docker Image Analysis](https://github.com/wagoodman/dive)
- [Hadolint - Dockerfile Linter](https://github.com/hadolint/hadolint)
- [Trivy - Security Scanner](https://github.com/aquasecurity/trivy)
- [act - Run GitHub Actions Locally](https://github.com/nektos/act)

### Plataformas de Deployment

- [Railway](https://railway.app/) - PaaS moderno
- [Render](https://render.com/) - Deploy desde GitHub
- [Fly.io](https://fly.io/) - Edge computing
- [AWS ECS](https://aws.amazon.com/ecs/) - Container orchestration
- [Google Cloud Run](https://cloud.google.com/run) - Serverless containers

---

## 📖 Artículos Recomendados

### Docker

1. **"Docker for Python Developers"** - Real Python
   - [realpython.com/docker-python](https://realpython.com/docker-in-action-fitter-happier-more-productive/)

2. **"Optimizing Docker Images"** - Docker Blog
   - [docker.com/blog/intro-guide-to-dockerfile-best-practices](https://www.docker.com/blog/intro-guide-to-dockerfile-best-practices/)

3. **"Multi-stage Builds"** - Docker Docs
   - [docs.docker.com/build/building/multi-stage](https://docs.docker.com/build/building/multi-stage/)

### CI/CD

1. **"CI/CD Best Practices"** - GitLab
   - [docs.gitlab.com/ee/ci/pipelines/pipeline_efficiency](https://docs.gitlab.com/ee/ci/pipelines/pipeline_efficiency.html)

2. **"GitHub Actions Workflows"** - GitHub Blog
   - [github.blog/2022-02-02-build-ci-cd-pipeline-github-actions](https://github.blog/2022-02-02-build-ci-cd-pipeline-github-actions-four-steps/)

---

## 🛠️ Cheat Sheets

### Docker Commands

```bash
# Images
docker build -t myapp .
docker images
docker rmi image_name

# Containers
docker run -d -p 8000:8000 myapp
docker ps -a
docker stop container_id
docker rm container_id

# Compose
docker compose up -d
docker compose down
docker compose logs -f
docker compose exec service_name bash

# Cleanup
docker system prune -a
docker volume prune
```

### GitHub Actions Syntax

```yaml
# Triggers
on:
  push:
    branches: [main]
  pull_request:
  schedule:
    - cron: '0 0 * * *'

# Jobs
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: echo "Hello"

# Matrix
strategy:
  matrix:
    python-version: [3.12, 3.13]

# Secrets
${{ secrets.MY_SECRET }}

# Conditions
if: github.event_name == 'push'
```
