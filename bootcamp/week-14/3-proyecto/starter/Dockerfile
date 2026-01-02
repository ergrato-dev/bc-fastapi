FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_SYSTEM_PYTHON=1

# Instalar uv
RUN pip install --no-cache-dir uv

WORKDIR /app

# Copiar dependencias
COPY pyproject.toml ./

# Instalar dependencias
RUN uv sync --no-dev

# Copiar código fuente
COPY . .

EXPOSE 8000

# Comando por defecto
CMD ["uv", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
