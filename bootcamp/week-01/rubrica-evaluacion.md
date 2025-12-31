# 📊 Rúbrica de Evaluación - Semana 1

## Introducción a Python Moderno y FastAPI

---

## 🎯 Competencias a Evaluar

| Competencia | Descripción |
|-------------|-------------|
| **C1** | Configurar entorno de desarrollo con Docker |
| **C2** | Aplicar type hints en código Python |
| **C3** | Implementar funciones asíncronas |
| **C4** | Crear endpoints básicos con FastAPI |

---

## 🧠 Conocimiento (30%)

### Cuestionario Teórico (20%)

| Criterio | Excelente (100%) | Bueno (80%) | Suficiente (70%) | Insuficiente (<70%) |
|----------|------------------|-------------|------------------|---------------------|
| Type hints | Explica correctamente todos los tipos básicos y Union | Explica la mayoría de tipos | Conoce tipos básicos | No comprende type hints |
| Async/Await | Explica el event loop y cuándo usar async | Entiende async básico | Sabe la sintaxis | No comprende async |
| FastAPI | Conoce decoradores, path/query params | Conoce endpoints básicos | Sabe crear GET | No sabe crear endpoints |
| Docker | Entiende Dockerfile y compose | Sabe usar comandos básicos | Puede levantar contenedor | No maneja Docker |

### Identificación de Errores (10%)

| Criterio | Puntos |
|----------|--------|
| Identifica 5/5 errores de tipado | 100% |
| Identifica 4/5 errores de tipado | 80% |
| Identifica 3/5 errores de tipado | 70% |
| Identifica <3 errores de tipado | <70% |

---

## 💪 Desempeño (40%)

### Ejercicios Prácticos

| Ejercicio | Peso | Criterios de Evaluación |
|-----------|------|------------------------|
| **Setup Docker** | 10% | Contenedor levanta, FastAPI responde en localhost |
| **Type Hints** | 10% | Funciones correctamente tipadas, sin errores de mypy |
| **Async/Await** | 10% | Funciones async funcionan, entiende await |
| **Primera API** | 10% | Endpoints funcionan, documentación accesible |

### Criterios por Ejercicio

| Nivel | Descripción | Porcentaje |
|-------|-------------|------------|
| **Excelente** | Código limpio, bien tipado, funcional, con comentarios | 100% |
| **Bueno** | Código funcional con type hints correctos | 80% |
| **Suficiente** | Código funcional con type hints básicos | 70% |
| **Insuficiente** | Código no funciona o sin type hints | <70% |

---

## 📦 Producto (30%)

### Proyecto: API de Saludo

| Criterio | Peso | Excelente (100%) | Bueno (80%) | Suficiente (70%) | Insuficiente (<70%) |
|----------|------|------------------|-------------|------------------|---------------------|
| **Funcionalidad** | 10% | API completa con GET y POST, manejo de errores | GET y POST funcionan | Solo GET funciona | No funciona |
| **Type Hints** | 8% | Todo el código tipado correctamente | 80% tipado | Tipado básico | Sin type hints |
| **Documentación** | 5% | Swagger completo con ejemplos | Swagger funcional | Swagger básico | Sin documentación |
| **Docker** | 4% | docker-compose.yml optimizado | Docker funciona | Docker básico | No corre en Docker |
| **Código Limpio** | 3% | Nomenclatura inglés, comentarios claros | Código legible | Código funcional | Código desordenado |

---

## 📋 Checklist de Entrega

### Estructura Esperada del Proyecto

```
api-saludo/
├── docker-compose.yml
├── Dockerfile
├── .env.example
├── README.md
├── pyproject.toml
└── src/
    └── main.py
```

### Requisitos Mínimos

- [ ] API levanta en Docker con `docker compose up`
- [ ] Endpoint GET `/` devuelve mensaje de bienvenida
- [ ] Endpoint GET `/saludo/{nombre}` devuelve saludo personalizado
- [ ] Endpoint POST `/saludo` acepta JSON y devuelve saludo
- [ ] Documentación accesible en `/docs`
- [ ] Type hints en todas las funciones
- [ ] README con instrucciones de uso

---

## 🏆 Escala de Calificación

| Calificación | Rango | Descripción |
|--------------|-------|-------------|
| **Sobresaliente** | 90-100% | Supera expectativas, código ejemplar |
| **Notable** | 80-89% | Cumple todos los requisitos correctamente |
| **Aprobado** | 70-79% | Cumple requisitos mínimos |
| **No Aprobado** | <70% | No cumple requisitos mínimos |

---

## ⚠️ Criterios de No Aprobación Automática

- Código que no compila/ejecuta
- Plagio detectado
- Entrega fuera de plazo sin justificación
- No usar Docker según las instrucciones
- Código sin ningún type hint

---

## 📝 Formato de Entrega

1. **Repositorio**: Fork del bootcamp o repo personal
2. **Branch**: `week-01-proyecto`
3. **Commit message**: `feat(week-01): complete greeting API project`
4. **Fecha límite**: Según calendario del bootcamp

---

## 🔄 Retroalimentación

Después de la evaluación recibirás:

- ✅ Puntuación por cada criterio
- 💬 Comentarios específicos en el código
- 📈 Sugerencias de mejora
- 🎯 Puntos fuertes identificados
