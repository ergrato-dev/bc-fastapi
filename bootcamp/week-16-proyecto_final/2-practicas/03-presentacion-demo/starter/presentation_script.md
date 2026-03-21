# 📝 Script de Presentación

Usa esta plantilla para preparar tu presentación. Completa cada sección con tu información.

---

## 1. Introducción (1-2 minutos)

### Saludo
```
Hola, mi nombre es [TU NOMBRE].
Hoy les presento [NOMBRE DEL PROYECTO], 
una API para [PROBLEMA QUE RESUELVE].
```

### El Problema
```
El problema que resuelve es:
[Describe el problema en 2-3 oraciones]

Ejemplo:
"Muchos equipos tienen dificultad para organizar y dar seguimiento 
a sus tareas. La información está dispersa en diferentes herramientas 
y no hay visibilidad del progreso."
```

### La Solución
```
Mi solución es una API RESTful que permite:
- [Feature 1]
- [Feature 2]
- [Feature 3]

Ejemplo:
"Mi solución permite crear proyectos, asignar tareas a usuarios,
establecer prioridades y fechas límite, y tener todo centralizado."
```

---

## 2. Arquitectura (2-3 minutos)

### Stack Tecnológico
```
El proyecto está construido con:

Backend:
- Python 3.12+ con FastAPI
- SQLAlchemy 2.x como ORM
- PostgreSQL para persistencia
- Pydantic v2 para validación

DevOps:
- Docker y Docker Compose
- GitHub Actions para CI/CD
- [Plataforma de deployment]
```

### Estructura del Proyecto
```
La arquitectura sigue el patrón [MVC/Hexagonal/etc.]:

src/
├── routers/      → Endpoints de la API
├── services/     → Lógica de negocio
├── repositories/ → Acceso a datos
├── models/       → Modelos SQLAlchemy
└── schemas/      → Validación Pydantic

Esta separación me permite:
- [Beneficio 1: ej. testing aislado]
- [Beneficio 2: ej. fácil mantenimiento]
```

### Decisión Técnica Destacada
```
Una decisión técnica interesante fue:
[Describe una decisión y por qué la tomaste]

Ejemplo:
"Decidí usar paginación basada en cursor en lugar de offset
porque escala mejor cuando hay muchos registros."
```

---

## 3. Demo en Vivo (4-5 minutos)

### Flujo a Demostrar

Practica este flujo exacto antes de la presentación:

```
1. Mostrar documentación
   → Abrir /docs en el navegador
   → "Aquí está la documentación auto-generada"

2. Registro de usuario
   → POST /auth/register
   → Mostrar validación de email y password

3. Login
   → POST /auth/login
   → Obtener token JWT
   → "El token tiene expiración de X minutos"

4. Crear recurso principal
   → POST /[tu-recurso] (ej: /tasks, /products)
   → Mostrar validación de campos

5. Listar recursos
   → GET /[tu-recurso]
   → Mostrar paginación funcionando

6. Mostrar relación
   → GET /[recurso-con-relacion]
   → "Aquí se ve cómo carga los datos relacionados"

7. Probar caso de error
   → Intentar acción sin autorización
   → Mostrar manejo de errores
```

### Puntos a Destacar Durante Demo
```
- "Noten cómo la validación..."
- "El error retorna un formato consistente..."
- "La paginación incluye total y metadata..."
- "Aquí uso [patrón/técnica] para..."
```

---

## 4. Código Destacado (2-3 minutos)

### Fragmento 1: [Nombre]
```python
# Muestra un fragmento de código interesante
# Explica qué hace y por qué es relevante

# Ejemplo: Dependency de autenticación
async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
) -> User:
    """
    Este es mi sistema de autenticación.
    Usa JWT con verificación de firma y expiración.
    """
    ...
```

```
"Este fragmento muestra cómo implementé [X].
Lo elegí porque [razón técnica]."
```

### Fragmento 2: [Nombre]
```python
# Otro fragmento interesante
# Puede ser: validación compleja, query optimizada, patrón de diseño

# Ejemplo: Validación Pydantic avanzada
class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    due_date: datetime | None = None
    
    @field_validator("due_date")
    def due_date_must_be_future(cls, v):
        if v and v < datetime.now():
            raise ValueError("Due date must be in the future")
        return v
```

```
"Aquí uso Pydantic para validar que [X].
Esto previene [problema] antes de llegar a la base de datos."
```

---

## 5. Cierre (1-2 minutos)

### Aprendizajes Clave
```
Durante este proyecto aprendí:

1. [Aprendizaje técnico]
   Ejemplo: "Cómo estructurar una API siguiendo clean architecture"

2. [Aprendizaje de proceso]
   Ejemplo: "La importancia de escribir tests desde el inicio"

3. [Aprendizaje personal]
   Ejemplo: "A no sobre-ingeniar soluciones desde el día uno"
```

### Desafíos Superados
```
El mayor desafío fue:
[Describe un problema y cómo lo resolviste]

Ejemplo:
"Tuve problemas con N+1 queries al cargar tareas con sus proyectos.
Lo resolví usando selectinload de SQLAlchemy."
```

### Mejoras Futuras
```
Si tuviera más tiempo, agregaría:
- [Mejora 1]
- [Mejora 2]
- [Mejora 3]

Ejemplo:
- Cache con Redis para endpoints frecuentes
- WebSockets para notificaciones en tiempo real
- Rate limiting por usuario
```

### Cierre
```
Eso es todo. El código está en GitHub en [URL].
La API está desplegada en [URL].
¿Preguntas?
```

---

## 📊 Notas de Tiempo

| Sección | Tiempo Target | Mi Tiempo |
|---------|---------------|-----------|
| Introducción | 1-2 min | ___ min |
| Arquitectura | 2-3 min | ___ min |
| Demo | 4-5 min | ___ min |
| Código | 2-3 min | ___ min |
| Cierre | 1-2 min | ___ min |
| **Total** | **10-15 min** | **___ min** |

---

## 💡 Tips

1. **Practica la demo 3+ veces** - Los errores en vivo son estresantes
2. **Ten datos de prueba listos** - No improvises datos durante la demo
3. **Prepara un plan B** - Si algo falla, ten screenshots o video
4. **Habla despacio** - Los nervios aceleran el habla
5. **Mira a la audiencia** - No solo a la pantalla
