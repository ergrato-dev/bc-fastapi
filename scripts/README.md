# 🔄 Auto-commit Scripts

Scripts para automatizar commits en el repositorio del bootcamp.

## 📋 Archivos

| Archivo | Descripción |
|---------|-------------|
| `autocommit.sh` | Script principal de auto-commit |
| `install-autocommit.sh` | Instalador del timer systemd (Fedora 43) |
| `logs/` | Directorio de logs (auto-generado) |

## 🚀 Instalación (Fedora 43)

```bash
# Dar permisos de ejecución
chmod +x scripts/*.sh

# Instalar con intervalo por defecto (30 minutos)
./scripts/install-autocommit.sh install

# Instalar con intervalo personalizado
./scripts/install-autocommit.sh install 1h    # Cada hora
./scripts/install-autocommit.sh install 15min # Cada 15 minutos
```

## 📊 Comandos Útiles

```bash
# Ver estado del timer
./scripts/install-autocommit.sh status

# Ejecutar manualmente
./scripts/install-autocommit.sh run

# Desinstalar
./scripts/install-autocommit.sh uninstall
```

## 🏷️ Formato de Commits

El script genera commits siguiendo **Conventional Commits** en inglés:

```
type(scope): what

What: description of changes
For: purpose of changes  
Impact: effect on project/users

Auto-committed by bc-fastapi autocommit script
```

### Tipos Detectados

| Tipo | Condición |
|------|-----------|
| `feat` | Archivos en `2-practicas/`, `3-proyecto/`, `*.py` |
| `docs` | Archivos en `1-teoria/`, `4-recursos/`, `5-glosario/`, `*.md` |
| `fix` | Archivos con "fix", "bug", "error" en el nombre |
| `chore` | Archivos de configuración, `scripts/` |
| `ci` | Archivos en `.github/` |
| `test` | Archivos de test |
| `refactor` | Archivos con "refactor" en el nombre |

### Scope Detectado

- `week-XX` - Cambios en una semana específica
- `docs` - Cambios en `docs/`
- `scripts` - Cambios en `scripts/`
- `assets` - Cambios en `assets/`
- `github` - Cambios en `.github/`

## 📝 Ejemplo de Commit Generado

```
feat(week-03): update 2 files

What: update 2 files
For: add new content for students
Impact: students can access new learning materials

Auto-committed by bc-fastapi autocommit script
```

## 🔧 Comandos systemd

```bash
# Ver estado del timer
systemctl --user status bc-fastapi-autocommit.timer

# Ver logs del servicio
journalctl --user -u bc-fastapi-autocommit.service

# Ver próxima ejecución
systemctl --user list-timers bc-fastapi-autocommit.timer

# Parar temporalmente
systemctl --user stop bc-fastapi-autocommit.timer

# Reanudar
systemctl --user start bc-fastapi-autocommit.timer
```

## 📁 Logs

Los logs se guardan en `scripts/logs/autocommit.log` y se rotan automáticamente al alcanzar 1MB.

```bash
# Ver logs
tail -f scripts/logs/autocommit.log
```

## ⚠️ Notas

- El script intenta hacer push automáticamente
- Si falla el push (sin conexión/autenticación), el commit se mantiene local
- Requiere que git esté configurado con credenciales para push automático
