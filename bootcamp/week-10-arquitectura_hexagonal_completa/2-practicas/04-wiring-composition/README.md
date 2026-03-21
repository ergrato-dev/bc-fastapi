# 🔗 Práctica 04: Wiring & Composition

## 📋 Descripción

En esta práctica aprenderás a **componer** toda la aplicación en el **Composition Root**. Conectarás todas las capas, configurarás las dependencias y crearás la aplicación FastAPI completa.

---

## 🎯 Objetivos

- Implementar el Composition Root en main.py
- Crear factories de dependencias
- Configurar dependency injection con FastAPI
- Ensamblar la aplicación completa
- Verificar que todo funciona end-to-end

---

## 📁 Estructura del Ejercicio

```
04-wiring-composition/
├── README.md
└── starter/
    ├── pyproject.toml
    ├── .env.example
    └── src/
        ├── __init__.py
        ├── domain/                 # Completo
        ├── application/            # Completo
        ├── infrastructure/         # Completo
        │   ├── ...
        │   └── api/
        │       ├── dependencies.py  # Factories
        │       └── main.py          # Composition Root
        └── main.py                  # Entry point
```

---

## ⏱️ Duración Estimada

30 minutos

---

## ✅ Criterios de Éxito

- [ ] dependencies.py tiene factories para repositories y services
- [ ] main.py crea la aplicación FastAPI completa
- [ ] Los endpoints funcionan end-to-end
- [ ] La configuración se lee de .env
