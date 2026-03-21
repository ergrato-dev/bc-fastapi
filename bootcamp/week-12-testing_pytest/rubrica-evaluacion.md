# 📊 Rúbrica de Evaluación - Semana 12

## Testing con pytest y pytest-asyncio

---

## 🎯 Competencias a Evaluar

### 1. Conocimiento (30%)

| Criterio | Excelente (100%) | Bueno (75%) | Suficiente (50%) | Insuficiente (0%) |
|----------|------------------|-------------|------------------|-------------------|
| **Tipos de tests** | Distingue claramente unitarios, integración, E2E y sabe cuándo usar cada uno | Conoce los tipos pero confunde cuándo aplicarlos | Conoce solo tests unitarios | No distingue tipos de tests |
| **Fixtures** | Domina scope, yield, conftest y fixtures parametrizados | Usa fixtures básicas correctamente | Solo usa fixtures sin scope | No entiende fixtures |
| **Mocking** | Aplica mock, patch y MagicMock apropiadamente | Usa mocking básico | Usa mocking con dificultad | No sabe usar mocking |
| **Cobertura** | Entiende métricas y sabe interpretar reportes | Puede generar reportes de cobertura | Conoce el concepto pero no lo aplica | Desconoce cobertura |

### 2. Desempeño (40%)

| Criterio | Excelente (100%) | Bueno (75%) | Suficiente (50%) | Insuficiente (0%) |
|----------|------------------|-------------|------------------|-------------------|
| **Tests unitarios** | Tests aislados, rápidos, con assertions claras | Tests funcionales pero algo acoplados | Tests básicos que pasan | Tests que fallan o no existen |
| **Tests de API** | Usa TestClient/httpx, testea todos los casos | Testea happy path y algunos errores | Solo testea happy path | No testea endpoints |
| **Tests async** | Usa pytest-asyncio correctamente con fixtures async | Tests async básicos funcionando | Tests async con problemas | No logra tests async |
| **Organización** | conftest.py, estructura clara, naming correcto | Buena estructura con pequeños issues | Estructura básica | Tests desorganizados |

### 3. Producto (30%)

| Criterio | Excelente (100%) | Bueno (75%) | Suficiente (50%) | Insuficiente (0%) |
|----------|------------------|-------------|------------------|-------------------|
| **Cobertura** | >90% de cobertura | 80-90% de cobertura | 70-80% de cobertura | <70% de cobertura |
| **Tests verdes** | 100% tests pasan | >95% tests pasan | >85% tests pasan | <85% tests pasan |
| **Completitud** | Todos los endpoints testeados con edge cases | Endpoints principales testeados | Algunos endpoints sin tests | Muchos endpoints sin tests |
| **Calidad** | Tests mantenibles, DRY, bien documentados | Tests claros con algo de duplicación | Tests funcionales pero confusos | Tests difíciles de entender |

---

## 📝 Escala de Calificación

| Puntaje | Calificación | Descripción |
|---------|--------------|-------------|
| 90-100 | A | Excelente dominio de testing |
| 80-89 | B | Buen dominio con áreas de mejora |
| 70-79 | C | Competencia básica alcanzada |
| 60-69 | D | Necesita refuerzo significativo |
| 0-59 | F | No alcanza competencias mínimas |

---

## ✅ Checklist de Entrega

### Prácticas
- [ ] 01-primeros-tests: Tests básicos funcionando
- [ ] 02-fixtures-avanzados: Fixtures con scope y yield
- [ ] 03-testing-endpoints: Tests de API completos
- [ ] 04-mocking-dependencies: Mocks implementados

### Proyecto
- [ ] Tests unitarios para services
- [ ] Tests de integración para endpoints
- [ ] Tests de autenticación
- [ ] Fixtures en conftest.py
- [ ] Cobertura >80%
- [ ] `pytest` ejecuta sin errores
- [ ] Reporte de cobertura incluido

### Código
- [ ] Estructura de tests organizada
- [ ] Naming convention: `test_*.py` y `test_*`
- [ ] Assertions descriptivas
- [ ] Sin tests comentados o skipped sin razón

---

## 📊 Distribución de Puntos

```
Conocimiento (30%)
├── Tipos de tests ........... 8%
├── Fixtures ................. 8%
├── Mocking .................. 7%
└── Cobertura ................ 7%

Desempeño (40%)
├── Tests unitarios .......... 10%
├── Tests de API ............. 12%
├── Tests async .............. 10%
└── Organización ............. 8%

Producto (30%)
├── Cobertura >80% ........... 8%
├── Tests verdes ............. 8%
├── Completitud .............. 7%
└── Calidad .................. 7%

TOTAL: 100%
```

---

## 🎯 Criterios de Aprobación

- **Mínimo 70%** en cada categoría
- **Todos los tests deben pasar** (`pytest` sin errores)
- **Cobertura mínima: 80%**
- **Entrega a tiempo**

---

## 📌 Comandos de Verificación

```bash
# Ejecutar tests
uv run pytest tests/ -v

# Con cobertura
uv run pytest tests/ --cov=src --cov-report=html

# Solo tests rápidos (unitarios)
uv run pytest tests/unit/ -v

# Tests de integración
uv run pytest tests/integration/ -v

# Ver reporte de cobertura
open htmlcov/index.html
```
