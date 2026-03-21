# ✅ Checklist Pre-Demo

Revisa esta lista **30 minutos antes** de tu presentación.

---

## 🖥️ Ambiente de Demo

### Aplicación
- [ ] API corriendo localmente o en servidor de demo
- [ ] Base de datos con datos de prueba realistas
- [ ] Todos los servicios healthy (docker compose up)
- [ ] Logs limpios (no errores previos que confundan)

### Datos de Prueba
- [ ] Usuario de prueba creado: `demo@example.com`
- [ ] Contraseña conocida: `Demo123!`
- [ ] Al menos 5-10 registros de cada entidad
- [ ] Datos que cuenten una "historia" coherente

### URLs Listas
```
Documentación: http://localhost:8000/docs
API Base:      http://localhost:8000/api/v1
Health:        http://localhost:8000/health
GitHub:        https://github.com/[tu-usuario]/[tu-repo]
Deploy:        https://[tu-app].railway.app (o similar)
```

---

## 🌐 Navegador

### Pestañas Preparadas (en orden)
1. [ ] Swagger UI (/docs)
2. [ ] ReDoc (/redoc) - backup
3. [ ] GitHub repo - página principal
4. [ ] Deploy en producción (si aplica)

### Configuración
- [ ] Zoom al 100-125% para que se lea bien
- [ ] Modo oscuro si tu terminal es oscura
- [ ] Sin extensiones que muestren notificaciones
- [ ] Historial/favoritos que no te avergüencen 😅

---

## 💻 Editor de Código

### Archivos Abiertos (en orden)
1. [ ] `src/main.py` - Entry point
2. [ ] Un router importante (ej: `routers/tasks.py`)
3. [ ] Un schema interesante (ej: `schemas/task.py`)
4. [ ] El código que quieres mostrar

### Configuración
- [ ] Fuente legible (14-16px)
- [ ] Tema con buen contraste
- [ ] Sidebar cerrada o minimizada
- [ ] Sin errores/warnings en archivos a mostrar

---

## 🛡️ Plan B (Si Algo Falla)

### Screenshots Preparados
- [ ] Screenshot de /docs funcionando
- [ ] Screenshot de response exitoso
- [ ] Screenshot de código clave
- [ ] Diagrama de arquitectura

### Video de Respaldo
- [ ] Grabar demo completa antes (2-3 min)
- [ ] Tener video accesible rápidamente
- [ ] "Tuve un problema técnico, les muestro el video"

### Frases de Emergencia
```
Si la API no responde:
"Parece que hay un problema de conexión. 
Mientras se resuelve, les muestro el código..."

Si hay un error inesperado:
"Interesante, esto no debería pasar.
El error indica [X], lo cual se resolvería con [Y]..."

Si te quedas en blanco:
"Déjenme revisar mis notas un momento..."
(Respira, mira tu script)
```

---

## 📋 Prueba de Demo (15 min antes)

Ejecuta exactamente el flujo que harás:

### 1. Health Check
```bash
curl http://localhost:8000/health
# Debe retornar: {"status": "healthy"}
```
- [ ] ✅ Funciona

### 2. Registro
```bash
curl -X POST http://localhost:8000/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email": "test@demo.com", "password": "Test123!"}'
```
- [ ] ✅ Funciona (o error de "ya existe" si ya probaste)

### 3. Login
```bash
curl -X POST http://localhost:8000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "demo@example.com", "password": "Demo123!"}'
```
- [ ] ✅ Retorna token

### 4. Endpoint Protegido
```bash
curl http://localhost:8000/api/v1/tasks \
  -H "Authorization: Bearer [TOKEN]"
```
- [ ] ✅ Retorna lista de tareas

### 5. Crear Recurso
```bash
curl -X POST http://localhost:8000/api/v1/tasks \
  -H "Authorization: Bearer [TOKEN]" \
  -H "Content-Type: application/json" \
  -d '{"title": "Tarea de demo", "project_id": 1}'
```
- [ ] ✅ Crea recurso exitosamente

---

## 🎤 Tu Preparación

### Físico
- [ ] Agua cerca
- [ ] Postura cómoda
- [ ] Manos visibles (si es video)

### Mental
- [ ] Respiración profunda (3 veces)
- [ ] Recordar: errores son oportunidades de mostrar debugging
- [ ] Confiar en tu preparación

### Técnico
- [ ] Micrófono probado
- [ ] Cámara (si aplica) funcionando
- [ ] Compartir pantalla probado
- [ ] Notificaciones silenciadas (Slack, email, etc.)

---

## ⏱️ Timeline Pre-Presentación

| Tiempo | Acción |
|--------|--------|
| -30 min | Revisar este checklist |
| -20 min | Levantar servicios (docker compose up) |
| -15 min | Ejecutar prueba de demo completa |
| -10 min | Abrir pestañas y archivos necesarios |
| -5 min | Respirar, revisar notas |
| 0 min | ¡Presentar! 🚀 |

---

## 📝 Notas Personales

```
[Espacio para tus notas específicas]




```
