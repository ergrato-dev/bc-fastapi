# ⚙️ Configuración del Entorno

Antes de empezar el bootcamp necesitas tener un entorno de desarrollo funcionando. Tienes dos opciones:

## 🔀 Elige tu Opción

| | 🐳 Con Docker | 🐍 Sin Docker |
|---|---|---|
| **Dificultad inicial** | Baja | Media |
| **Consistencia** | ✅ Idéntico en todas las máquinas | ⚠️ Depende de tu sistema |
| **Requisitos** | Docker 27+ | Python 3.13+, uv |
| **Conflictos de versiones** | ✅ Imposibles | ⚠️ Posibles |
| **Velocidad de arranque** | ~30 s (primera vez) | ~5 s |
| **Recomendado para** | Todos los estudiantes | Máquinas sin Docker |

## ✅ Opción Recomendada: Docker

Docker es el entorno **oficial** del bootcamp. Garantiza que todos los estudiantes trabajen con exactamente las mismas versiones de Python, dependencias y servicios, independientemente del sistema operativo.

→ [Guía: Configuración con Docker](con-docker.md)

## 🔧 Opción Alternativa: Sin Docker

Si tu máquina no puede ejecutar Docker (recursos limitados, restricciones corporativas, etc.), puedes configurar un entorno local con Python y `uv`.

> ⚠️ **Advertencia**: Algunos ejercicios de semanas avanzadas (PostgreSQL, múltiples servicios) requieren Docker. Esta opción es válida para las primeras semanas.

→ [Guía: Configuración sin Docker](sin-docker.md)

---

## 📋 ¿Cuál Elegir?

```
¿Tienes Docker instalado o puedes instalarlo?
        │
        ├── SÍ ──► Usa la opción Docker (recomendada)
        │
        └── NO ──► ¿Tienes Python 3.13+ instalado o puedes instalarlo?
                        │
                        ├── SÍ ──► Usa la opción Sin Docker
                        │
                        └── NO ──► Instala pyenv + uv, luego usa Sin Docker
```

---

→ Volver a [docs/README.md](../README.md)
