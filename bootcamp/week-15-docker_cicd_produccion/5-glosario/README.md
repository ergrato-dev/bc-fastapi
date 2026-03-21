# 📚 Glosario - Semana 15: Docker, CI/CD y Producción

## A

### Artifact
Archivo o conjunto de archivos generados durante el proceso de build (imagen Docker, binario, etc.) que puede ser desplegado o almacenado.

### Alpine Linux
Distribución Linux minimalista (~5MB) frecuentemente usada como imagen base para contenedores por su pequeño tamaño.

---

## B

### Build Context
Directorio enviado al Docker daemon durante `docker build`. Define qué archivos están disponibles para la imagen.

```bash
docker build -t myapp .  # "." es el build context
```

### Build Stage
En multi-stage builds, cada instrucción `FROM` inicia un nuevo stage. Permite separar compilación de runtime.

---

## C

### CI/CD (Continuous Integration/Continuous Deployment)
Práctica de automatizar la integración, testing y despliegue de código. CI verifica cambios, CD los despliega.

### Container
Instancia ejecutable de una imagen Docker. Es un proceso aislado que comparte el kernel del host.

### Container Registry
Servicio para almacenar y distribuir imágenes Docker (Docker Hub, GitHub Container Registry, AWS ECR).

---

## D

### Dockerfile
Archivo de texto con instrucciones para construir una imagen Docker.

```dockerfile
FROM python:3.13-slim
WORKDIR /app
COPY . .
CMD ["python", "main.py"]
```

### Docker Compose
Herramienta para definir y ejecutar aplicaciones multi-contenedor usando un archivo YAML.

### Docker Daemon
Servicio en segundo plano que gestiona contenedores, imágenes, volúmenes y networks.

### Docker Image
Plantilla de solo lectura con instrucciones para crear un contenedor. Compuesta por capas (layers).

---

## E

### Entrypoint
Comando que se ejecuta cuando el contenedor inicia. Diferente de CMD, no se puede sobrescribir fácilmente.

```dockerfile
ENTRYPOINT ["python", "main.py"]
```

### Environment Variables
Variables de configuración pasadas al contenedor en tiempo de ejecución.

```yaml
environment:
  - DATABASE_URL=postgresql://...
```

---

## G

### GitHub Actions
Plataforma de CI/CD integrada en GitHub que ejecuta workflows automatizados.

### GitHub Container Registry (GHCR)
Registry de contenedores integrado en GitHub. URL: `ghcr.io/username/image`.

---

## H

### Healthcheck
Instrucción Docker que define cómo verificar si un contenedor está funcionando correctamente.

```dockerfile
HEALTHCHECK --interval=30s CMD curl -f http://localhost:8000/health
```

---

## I

### Image Layer
Cada instrucción en un Dockerfile crea una capa. Las capas se cachean para builds más rápidos.

---

## J

### Job
En GitHub Actions, unidad de trabajo que se ejecuta en un runner. Un workflow puede tener múltiples jobs.

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
```

---

## L

### Liveness Probe
Check que determina si un contenedor debe ser reiniciado. Usado por Kubernetes y Docker health checks.

---

## M

### Multi-stage Build
Técnica de Dockerfile que usa múltiples `FROM` para separar compilación de runtime, reduciendo tamaño de imagen.

```dockerfile
FROM node:20 AS builder
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
```

---

## N

### Network (Docker)
Red virtual que permite comunicación entre contenedores. Tipos: bridge, host, overlay, none.

### Non-root User
Usuario sin privilegios de root dentro del contenedor. Best practice de seguridad.

```dockerfile
RUN useradd -m appuser
USER appuser
```

---

## O

### OCI (Open Container Initiative)
Estándar abierto para formatos de contenedores e imágenes.

---

## P

### Pipeline
Secuencia de stages/jobs en un proceso CI/CD (build → test → deploy).

### Port Mapping
Mapeo de puertos entre host y contenedor.

```bash
docker run -p 8000:8000 myapp  # host:container
```

---

## R

### Readiness Probe
Check que determina si un contenedor está listo para recibir tráfico.

### Registry
Ver Container Registry.

### Runner
Máquina (VM o servidor) que ejecuta jobs de GitHub Actions.

---

## S

### Secret
Variable sensible (API keys, passwords) manejada de forma segura en CI/CD.

```yaml
${{ secrets.API_KEY }}
```

### Service (Docker Compose)
Definición de un contenedor en docker-compose.yml, incluyendo imagen, puertos, variables, etc.

### Stage
Ver Build Stage.

### Step
Tarea individual dentro de un job de GitHub Actions.

```yaml
steps:
  - uses: actions/checkout@v4
  - run: pip install -r requirements.txt
```

---

## T

### Tag (Docker)
Identificador de versión de una imagen Docker.

```bash
docker build -t myapp:v1.0.0 .
docker build -t myapp:latest .
```

### Trigger
Evento que inicia un workflow de GitHub Actions (push, pull_request, schedule, etc.).

### Trivy
Scanner de seguridad para contenedores, sistemas de archivos y repositorios.

---

## V

### Volume
Mecanismo para persistir datos generados por contenedores.

```yaml
volumes:
  - postgres_data:/var/lib/postgresql/data
```

---

## W

### Workflow
Archivo YAML que define automatizaciones en GitHub Actions. Se almacena en `.github/workflows/`.

```yaml
name: CI
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
```

---

## Y

### YAML
Formato de serialización de datos usado en docker-compose.yml y GitHub Actions workflows.

---

## 📖 Referencias

- [Docker Glossary](https://docs.docker.com/glossary/)
- [GitHub Actions Glossary](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions)
- [Kubernetes Glossary](https://kubernetes.io/docs/reference/glossary/)
