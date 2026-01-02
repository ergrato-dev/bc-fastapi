# 🧪 Semana 12: Testing con pytest y pytest-asyncio

## 📋 Descripción

Esta semana aprenderás a escribir **tests automatizados** para APIs FastAPI usando pytest. Cubriremos desde tests unitarios básicos hasta tests de integración con bases de datos, mocking, fixtures avanzados y testing de código asíncrono.

---

## 🎯 Objetivos de Aprendizaje

Al finalizar esta semana, serás capaz de:

- ✅ Configurar pytest y pytest-asyncio en proyectos FastAPI
- ✅ Escribir tests unitarios para funciones y clases
- ✅ Crear tests de integración para endpoints REST
- ✅ Usar fixtures para setup y teardown de tests
- ✅ Implementar mocking para aislar componentes
- ✅ Testear código asíncrono con pytest-asyncio
- ✅ Configurar bases de datos de prueba aisladas
- ✅ Medir cobertura de código con pytest-cov
- ✅ Aplicar Test-Driven Development (TDD) básico

---

## 📚 Contenido

### 1. Teoría

| Archivo | Tema | Duración |
|---------|------|----------|
| [01-fundamentos-testing.md](1-teoria/01-fundamentos-testing.md) | Pirámide de testing, tipos de tests | 20 min |
| [02-pytest-basico.md](1-teoria/02-pytest-basico.md) | Instalación, assertions, estructura | 25 min |
| [03-fixtures-y-parametrize.md](1-teoria/03-fixtures-y-parametrize.md) | Fixtures, scope, parametrización | 25 min |
| [04-testing-fastapi.md](1-teoria/04-testing-fastapi.md) | TestClient, httpx, async tests | 25 min |
| [05-mocking-y-patching.md](1-teoria/05-mocking-y-patching.md) | Mock, patch, MagicMock | 20 min |

### 2. Prácticas

| Práctica | Tema | Duración |
|----------|------|----------|
| [01-primeros-tests](2-practicas/01-primeros-tests/) | Tests básicos con pytest | 30 min |
| [02-fixtures-avanzados](2-practicas/02-fixtures-avanzados/) | Fixtures, conftest, scope | 30 min |
| [03-testing-endpoints](2-practicas/03-testing-endpoints/) | Tests de APIs con TestClient | 35 min |
| [04-mocking-dependencies](2-practicas/04-mocking-dependencies/) | Mock de servicios y DB | 30 min |

### 3. Proyecto

| Proyecto | Descripción | Duración |
|----------|-------------|----------|
| [Test Suite Completo](3-proyecto/) | Suite de tests para API de tareas | 90 min |

---

## ⏱️ Distribución del Tiempo

| Actividad | Tiempo |
|-----------|--------|
| Teoría | 2 horas |
| Prácticas | 2 horas |
| Proyecto | 1.5 horas |
| Revisión | 30 min |
| **Total** | **6 horas** |

---

## 📦 Herramientas de la Semana

```toml
[project.optional-dependencies]
dev = [
    "pytest>=8.3.4",
    "pytest-asyncio>=0.24.0",
    "pytest-cov>=6.0.0",
    "httpx>=0.28.0",
    "respx>=0.22.0",        # Mock HTTP requests
    "factory-boy>=3.3.0",   # Test factories
    "faker>=33.0.0",        # Fake data generation
]
```

---

## 🔑 Conceptos Clave

- **Test Unitario**: Prueba una unidad de código aislada
- **Test de Integración**: Prueba interacción entre componentes
- **Fixture**: Función que prepara datos/estado para tests
- **Mock**: Objeto simulado que reemplaza dependencias reales
- **Coverage**: Porcentaje de código ejecutado por tests
- **TDD**: Escribir tests antes del código de producción

---

## 📋 Requisitos Previos

- ✅ Semana 11: Autenticación JWT (para testear endpoints protegidos)
- ✅ Conocimiento de FastAPI y SQLAlchemy
- ✅ Comprensión de async/await en Python

---

## 📌 Entregables

1. **Prácticas completadas**: 4 ejercicios de testing
2. **Proyecto**: Suite de tests con >80% cobertura
3. **Tests pasando**: `pytest` sin errores

---

## 🔗 Navegación

| ← Anterior | Inicio | Siguiente → |
|:-----------|:------:|------------:|
| [Semana 11: JWT Auth](../week-11/README.md) | [Bootcamp](../../README.md) | [Semana 13: WebSockets](../week-13/README.md) |

---

## 📚 Recursos Adicionales

- [4-recursos/ebooks-free/](4-recursos/ebooks-free/) - Libros gratuitos
- [4-recursos/videografia/](4-recursos/videografia/) - Videos recomendados
- [4-recursos/webgrafia/](4-recursos/webgrafia/) - Enlaces útiles
- [5-glosario/](5-glosario/) - Términos clave de testing
