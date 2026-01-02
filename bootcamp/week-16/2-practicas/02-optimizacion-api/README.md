# ⚡ Práctica 02: Optimización de API

## 📋 Descripción

En esta práctica aprenderás técnicas para **optimizar el rendimiento** de tu API FastAPI. Identificarás cuellos de botella y aplicarás mejoras.

---

## 🎯 Objetivos

1. Identificar problemas de rendimiento (N+1, queries lentas)
2. Implementar caching básico
3. Optimizar queries de base de datos
4. Aplicar compresión de respuestas

---

## ⏱️ Duración

~45 minutos

---

## 📚 Conceptos Clave

### Problemas Comunes de Rendimiento

1. **N+1 Queries**: Hacer N queries adicionales por cada elemento
2. **Queries sin índices**: Escaneos completos de tabla
3. **Datos innecesarios**: Cargar más de lo necesario
4. **Sin paginación**: Retornar miles de registros
5. **Operaciones síncronas**: Bloquear I/O

### Herramientas de Diagnóstico

- **SQLAlchemy echo**: Ver queries ejecutadas
- **Logging de tiempo**: Medir duración de operaciones
- **Profilers**: cProfile, py-spy

---

## 🛠️ Paso a Paso

### Paso 1: Identificar N+1 Queries

Abre `starter/n_plus_one.py` para ver ejemplos de N+1 y cómo solucionarlos.

### Paso 2: Configurar Logging de Queries

En `starter/query_logging.py` aprende a monitorear queries de SQLAlchemy.

### Paso 3: Implementar Caching Simple

En `starter/caching.py` implementa un cache en memoria básico.

### Paso 4: Optimizar Endpoints

Aplica las técnicas aprendidas a `starter/optimize_endpoints.py`.

---

## 📁 Archivos

```
02-optimizacion-api/
├── README.md
└── starter/
    ├── n_plus_one.py
    ├── query_logging.py
    ├── caching.py
    └── optimize_endpoints.py
```

---

## ✅ Criterios de Éxito

- [ ] N+1 queries identificados y corregidos
- [ ] Logging de queries configurado
- [ ] Cache básico implementado
- [ ] Al menos 2 endpoints optimizados
