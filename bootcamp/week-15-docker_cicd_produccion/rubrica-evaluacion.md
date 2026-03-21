# 📋 Rúbrica de Evaluación - Semana 15

## Docker, CI/CD y Preparación para Producción

### 📊 Distribución de Puntos

| Competencia | Descripción | Puntos |
|-------------|-------------|--------|
| CE1 | Containerización con Docker | 25 |
| CE2 | Orquestación con Docker Compose | 20 |
| CE3 | CI/CD con GitHub Actions | 25 |
| CE4 | Deployment y Configuración | 20 |
| CE5 | Mejores Prácticas y Documentación | 10 |
| **Total** | | **100** |

---

## 🎯 CE1: Containerización con Docker (25 puntos)

### Excelente (23-25 pts)
- ✅ Dockerfile con multi-stage build correctamente implementado
- ✅ Imagen final optimizada (<150MB para Python slim)
- ✅ Usuario no-root configurado para seguridad
- ✅ .dockerignore completo y apropiado
- ✅ Labels de metadatos (maintainer, version)
- ✅ Healthcheck configurado en Dockerfile
- ✅ Caché de capas aprovechado eficientemente

### Bueno (18-22 pts)
- ✅ Dockerfile funcional con multi-stage build
- ✅ Imagen razonablemente optimizada (<300MB)
- ✅ Usuario no-root o .dockerignore presente
- ⚠️ Algunas optimizaciones faltantes
- ✅ Healthcheck básico

### Suficiente (13-17 pts)
- ✅ Dockerfile funcional sin multi-stage
- ⚠️ Imagen grande pero funcional
- ⚠️ Sin usuario no-root
- ⚠️ .dockerignore incompleto
- ✅ Contenedor ejecuta correctamente

### Insuficiente (0-12 pts)
- ❌ Dockerfile con errores
- ❌ Imagen no construye o falla
- ❌ Sin consideraciones de seguridad
- ❌ Sin optimizaciones

---

## 🎯 CE2: Orquestación con Docker Compose (20 puntos)

### Excelente (18-20 pts)
- ✅ docker-compose.yml con todos los servicios necesarios
- ✅ Redes personalizadas configuradas
- ✅ Volúmenes persistentes para datos
- ✅ Variables de entorno externalizadas (.env)
- ✅ Healthchecks en servicios
- ✅ Dependencias entre servicios (depends_on con condition)
- ✅ Restart policies configuradas

### Bueno (14-17 pts)
- ✅ docker-compose.yml funcional con API + DB
- ✅ Variables de entorno en archivo .env
- ✅ Volúmenes para persistencia
- ⚠️ Redes implícitas (default)
- ⚠️ Sin healthchecks en compose

### Suficiente (10-13 pts)
- ✅ docker-compose.yml básico funcional
- ⚠️ Variables hardcodeadas
- ⚠️ Sin volúmenes persistentes
- ⚠️ Sin configuración de redes
- ✅ Servicios se comunican

### Insuficiente (0-9 pts)
- ❌ docker-compose.yml con errores
- ❌ Servicios no se comunican
- ❌ Sin variables de entorno
- ❌ No levanta correctamente

---

## 🎯 CE3: CI/CD con GitHub Actions (25 puntos)

### Excelente (23-25 pts)
- ✅ Workflow completo con múltiples jobs
- ✅ Tests automatizados ejecutándose
- ✅ Linting con ruff configurado
- ✅ Type checking con mypy
- ✅ Build de imagen Docker
- ✅ Escaneo de seguridad (trivy o similar)
- ✅ Caché de dependencias configurado
- ✅ Matrix testing (múltiples versiones Python)
- ✅ Secrets gestionados correctamente

### Bueno (18-22 pts)
- ✅ Workflow con tests y lint
- ✅ Build de Docker funcionando
- ✅ Caché de dependencias
- ⚠️ Sin matrix testing
- ⚠️ Sin escaneo de seguridad
- ✅ Jobs bien estructurados

### Suficiente (13-17 pts)
- ✅ Workflow básico que ejecuta tests
- ⚠️ Sin lint o type checking
- ⚠️ Sin build de Docker en CI
- ⚠️ Sin caché
- ✅ Se ejecuta en push/PR

### Insuficiente (0-12 pts)
- ❌ Workflow con errores de sintaxis
- ❌ Jobs fallan consistentemente
- ❌ Sin tests en CI
- ❌ No se ejecuta correctamente

---

## 🎯 CE4: Deployment y Configuración (20 puntos)

### Excelente (18-20 pts)
- ✅ Configuración lista para múltiples entornos (dev/staging/prod)
- ✅ Variables de entorno documentadas
- ✅ Guía de deployment clara y completa
- ✅ Configuración de al menos un servicio cloud
- ✅ Base de datos de producción configurada
- ✅ HTTPS/SSL considerado
- ✅ Migraciones automatizadas

### Bueno (14-17 pts)
- ✅ Configuración para producción funcional
- ✅ Variables de entorno externalizadas
- ✅ Documentación de deployment básica
- ⚠️ Un solo entorno configurado
- ✅ Conexión a DB externa funciona

### Suficiente (10-13 pts)
- ✅ App puede desplegarse manualmente
- ⚠️ Configuración parcialmente documentada
- ⚠️ Variables de entorno mezcladas
- ⚠️ Sin guía de deployment clara
- ✅ Funciona en entorno local

### Insuficiente (0-9 pts)
- ❌ No se puede desplegar
- ❌ Configuración incompleta
- ❌ Sin documentación
- ❌ Hardcoded credentials

---

## 🎯 CE5: Mejores Prácticas y Documentación (10 puntos)

### Excelente (9-10 pts)
- ✅ README completo con instrucciones claras
- ✅ .dockerignore optimizado
- ✅ .gitignore apropiado
- ✅ Comentarios en Dockerfile explicativos
- ✅ Diagrama de arquitectura incluido
- ✅ Troubleshooting documentado

### Bueno (7-8 pts)
- ✅ README con instrucciones básicas
- ✅ .dockerignore presente
- ✅ Comentarios en archivos principales
- ⚠️ Sin diagrama de arquitectura

### Suficiente (5-6 pts)
- ✅ README mínimo
- ⚠️ .dockerignore incompleto
- ⚠️ Pocos comentarios
- ⚠️ Instrucciones ambiguas

### Insuficiente (0-4 pts)
- ❌ Sin README o muy incompleto
- ❌ Sin .dockerignore
- ❌ Sin documentación
- ❌ Código sin comentarios

---

## 📝 Criterios de Aprobación

| Requisito | Mínimo |
|-----------|--------|
| Puntuación total | ≥ 70/100 |
| CE1 (Containerización) | ≥ 13/25 |
| CE2 (Orquestación) | ≥ 10/20 |
| CE3 (CI/CD) | ≥ 13/25 |
| CE4 (Deployment) | ≥ 10/20 |
| Entrega | Antes del deadline |

---

## 📦 Entregables Requeridos

### Obligatorios
1. **Dockerfile** optimizado con multi-stage build
2. **docker-compose.yml** con stack completo
3. **.github/workflows/ci.yml** con pipeline funcional
4. **README.md** con instrucciones de uso
5. **.env.example** con variables documentadas

### Opcionales (Puntos Extra)
- Deploy funcional en Railway/Render (+5 pts)
- CD automático al hacer merge a main (+5 pts)
- Escaneo de vulnerabilidades con Trivy (+3 pts)
- Notificaciones de Slack/Discord en CI (+2 pts)

---

## 🔍 Checklist de Evaluación

### Dockerfile
- [ ] Usa imagen base oficial (python:3.13-slim)
- [ ] Multi-stage build implementado
- [ ] Usuario no-root configurado
- [ ] WORKDIR establecido
- [ ] COPY optimizado para caché
- [ ] Dependencias instaladas correctamente
- [ ] Puerto expuesto (EXPOSE)
- [ ] CMD/ENTRYPOINT definido
- [ ] .dockerignore presente

### Docker Compose
- [ ] Versión especificada
- [ ] Servicio API configurado
- [ ] Servicio DB configurado
- [ ] Red personalizada (opcional pero recomendado)
- [ ] Volúmenes persistentes
- [ ] Variables de entorno en .env
- [ ] Puertos mapeados correctamente
- [ ] depends_on configurado

### GitHub Actions
- [ ] Trigger en push y pull_request
- [ ] Job de tests
- [ ] Job de lint/format
- [ ] Job de build Docker
- [ ] Caché de pip/uv configurado
- [ ] Secrets no expuestos
- [ ] Status badges (opcional)

### Documentación
- [ ] README con Quick Start
- [ ] Variables de entorno documentadas
- [ ] Comandos de desarrollo
- [ ] Comandos de producción
- [ ] Troubleshooting básico

---

## 📊 Escala de Calificación

| Rango | Calificación | Descripción |
|-------|--------------|-------------|
| 90-100 | A | Excelente - Production-ready |
| 80-89 | B | Bueno - Funcional con mejoras menores |
| 70-79 | C | Suficiente - Cumple requisitos mínimos |
| 60-69 | D | Insuficiente - Requiere correcciones |
| 0-59 | F | No aprobado - Rehacer |

---

_Rúbrica Semana 15 · Docker, CI/CD y Producción_
