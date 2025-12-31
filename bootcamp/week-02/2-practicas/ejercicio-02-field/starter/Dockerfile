FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_SYSTEM_PYTHON=1

RUN pip install --no-cache-dir uv

WORKDIR /app
COPY pyproject.toml .
RUN uv sync --frozen 2>/dev/null || uv sync

COPY . .

CMD ["uv", "run", "python", "main.py"]
