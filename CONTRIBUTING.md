# 🤝 Guía de Contribución

¡Gracias por tu interés en contribuir al **Bootcamp FastAPI - Zero to Hero**! Este documento proporciona las pautas para contribuir al proyecto.

## 📋 Tabla de Contenidos

- [Código de Conducta](#código-de-conducta)
- [¿Cómo Puedo Contribuir?](#cómo-puedo-contribuir)
- [Configuración del Entorno](#configuración-del-entorno)
- [Flujo de Trabajo](#flujo-de-trabajo)
- [Convenciones de Código](#convenciones-de-código)
- [Commits](#commits)
- [Pull Requests](#pull-requests)

---

## 📜 Código de Conducta

Este proyecto se adhiere al [Código de Conducta](CODE_OF_CONDUCT.md). Al participar, se espera que respetes este código. Por favor, reporta comportamientos inaceptables.

---

## 🎯 ¿Cómo Puedo Contribuir?

### 🐛 Reportar Bugs

Si encuentras un bug, por favor abre un [Issue](https://github.com/epti-dev/bc-fastapi/issues/new?template=bug_report.md) incluyendo:

- Descripción clara del problema
- Pasos para reproducirlo
- Comportamiento esperado vs actual
- Screenshots si aplica
- Información del entorno (OS, versiones, etc.)

### 💡 Sugerir Mejoras

Las sugerencias de mejoras son bienvenidas. Abre un [Issue](https://github.com/epti-dev/bc-fastapi/issues/new?template=feature_request.md) describiendo:

- El problema que resuelve
- La solución propuesta
- Alternativas consideradas
- Contexto adicional

### 📚 Mejorar Documentación

- Correcciones ortográficas o gramaticales
- Clarificación de explicaciones
- Nuevos ejemplos de código
- Traducciones

### ✨ Contribuir Código

- Nuevos ejercicios o prácticas
- Mejoras en el código existente
- Tests adicionales
- Recursos visuales (diagramas SVG)

---

## ⚙️ Configuración del Entorno

### Prerrequisitos

- Docker y Docker Compose
- Git
- VS Code (recomendado)

### Setup

```bash
# 1. Fork del repositorio en GitHub

# 2. Clonar tu fork
git clone https://github.com/TU-USUARIO/bc-fastapi.git
cd bc-fastapi

# 3. Agregar upstream
git remote add upstream https://github.com/epti-dev/bc-fastapi.git

# 4. Abrir en VS Code
code .
```

---

## 🔄 Flujo de Trabajo

### 1. Sincronizar con upstream

```bash
git fetch upstream
git checkout main
git merge upstream/main
```

### 2. Crear una rama

```bash
# Para features
git checkout -b feature/nombre-descriptivo

# Para bugs
git checkout -b fix/descripcion-del-bug

# Para docs
git checkout -b docs/que-se-documenta
```

### 3. Hacer cambios

- Sigue las convenciones de código
- Escribe tests si aplica
- Actualiza la documentación si es necesario

### 4. Commit y Push

```bash
git add .
git commit -m "tipo: descripción breve"
git push origin nombre-de-tu-rama
```

### 5. Crear Pull Request

- Ve a GitHub y crea un PR hacia `main`
- Completa la plantilla del PR
- Espera la revisión

---

## 📝 Convenciones de Código

### Python

```python
# ✅ CORRECTO
async def get_user_by_id(user_id: int) -> User | None:
    """Fetch user from database by ID."""
    return await db.query(User).filter(User.id == user_id).first()

# ❌ INCORRECTO
def getUser(id):
    return db.query(User).filter(User.id == id).first()
```

### Reglas Generales

| Elemento | Convención |
|----------|------------|
| Variables/funciones | `snake_case` |
| Clases | `PascalCase` |
| Constantes | `UPPER_SNAKE_CASE` |
| Archivos | `snake_case.py` |
| Type hints | **Obligatorios** |
| Docstrings | En inglés |

### Documentación

- READMEs y guías en **español**
- Código y comentarios técnicos en **inglés**
- Comentarios educativos en **español** cuando expliquen conceptos

---

## 💬 Commits

Usamos [Conventional Commits](https://www.conventionalcommits.org/):

```
tipo(scope): descripción breve

[cuerpo opcional]

[footer opcional]
```

### Tipos Permitidos

| Tipo | Descripción |
|------|-------------|
| `feat` | Nueva funcionalidad |
| `fix` | Corrección de bug |
| `docs` | Solo documentación |
| `style` | Formato (no afecta código) |
| `refactor` | Refactorización |
| `test` | Agregar o modificar tests |
| `chore` | Tareas de mantenimiento |

### Ejemplos

```bash
feat(week-03): add SQLAlchemy introduction exercises
fix(week-01): correct typo in async/await explanation
docs(readme): update installation instructions
chore(deps): update fastapi to 0.110.0
```

---

## 🔀 Pull Requests

### Checklist

Antes de crear un PR, asegúrate de:

- [ ] El código sigue las convenciones del proyecto
- [ ] Has agregado tests (si aplica)
- [ ] La documentación está actualizada
- [ ] Los commits siguen Conventional Commits
- [ ] Has probado los cambios localmente
- [ ] No hay conflictos con `main`

### Plantilla

Al crear un PR, completa la plantilla proporcionada:

- **Descripción**: ¿Qué hace este PR?
- **Tipo de cambio**: feat/fix/docs/etc.
- **Testing**: ¿Cómo se probó?
- **Screenshots**: Si hay cambios visuales
- **Issues relacionados**: `Closes #123`

### Revisión

- Al menos 1 aprobación requerida
- Los CI checks deben pasar
- Sin conflictos de merge

---

## 🎨 Recursos Visuales

### Diagramas

- **Formato**: SVG preferido
- **Tema**: Dark mode
- **Colores**: Paleta FastAPI (#009688)
- **Sin degradés** (gradients)

### Screenshots

- PNG o JPG
- Anotaciones claras
- Optimizados antes de subir

---

## ❓ ¿Preguntas?

- 💬 [GitHub Discussions](https://github.com/epti-dev/bc-fastapi/discussions)
- 🐛 [GitHub Issues](https://github.com/epti-dev/bc-fastapi/issues)

---

¡Gracias por contribuir! 🚀
