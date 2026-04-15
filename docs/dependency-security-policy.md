# 🔒 Política de Seguridad en Dependencias

> **Audiencia**: Instructores, contributors y mantenedores del bootcamp.

---

## 🥇 Regla de Oro: SIEMPRE versiones exactas con `==`

```toml
# ✅ CORRECTO — versión exacta, reproducible y auditable
dependencies = [
    "fastapi==0.128.0",
    "sqlalchemy==2.0.46",
    "pydantic==2.12.0",
]

# ❌ PROHIBIDO — rango abierto, deja entrar versiones vulnerables sin aviso
dependencies = [
    "fastapi>=0.128.0",   # ← instala la más nueva, puede romper el bootcamp
    "sqlalchemy^2.0.46",  # ← notación Poetry/npm, no válida en pyproject.toml
    "pydantic",           # ← sin versión, completamente impredecible
]
```

### ¿Por qué no `>=`?

| Especificador | Problema |
|---|---|
| `>=X.Y.Z` | Instala la última disponible; puede traer una versión con CVE o breaking changes |
| `^X.Y.Z` | Notación Poetry/npm. **Inválida en pyproject.toml estándar (PEP 508)** |
| Sin versión | No reproducible. Cada `uv sync` puede dar un resultado diferente |
| `==X.Y.*` | Permite parches que pueden incluir cambios de comportamiento |

### ¿Por qué sí `==`?

- **Reproducibilidad**: todos los estudiantes instalan exactamente lo mismo
- **Auditabilidad**: se puede revisar CVEs para una versión específica
- **Estabilidad**: el código del bootcamp siempre funciona igual
- **Seguridad**: actualizaciones son decisiones conscientes y revisadas

---

## 🚨 Auditoría CVE — Abril 2026

Auditoría exhaustiva realizada el 04/04/2026 con **pip-audit** y base de datos **GitHub Advisory / OSV**.

### Vulnerabilidades encontradas y corregidas

| Paquete | CVE | Severidad | CVSS | Versión vulnerable | Versión segura |
|---|---|---|---|---|---|
| `python-jose` | [CVE-2024-33663](https://github.com/advisories/GHSA-6c5p-j8vq-pqhj) | **Crítica** | 9.3 | `< 3.4.0` | `== 3.5.0` |
| `python-jose` | [CVE-2024-33664](https://github.com/advisories/GHSA-cjwg-qfpm-7377) | Moderada | 5.3 | `< 3.4.0` | `== 3.5.0` |
| `python-multipart` | [CVE-2024-53981](https://github.com/advisories/GHSA-59g5-xgcq-4qw3) | Alta | 8.7 | `< 0.0.18` | `== 0.0.22` |
| `python-multipart` | [CVE-2026-24486](https://github.com/advisories/GHSA-wp53-j4wj-2cfg) | Alta | 8.6 | `< 0.0.22` | `== 0.0.22` |
| `jinja2` | [CVE-2025-27516](https://github.com/advisories/GHSA-cpwx-vrp4-4pq7) | Moderada | 5.4 | `<= 3.1.5` | `== 3.1.6` |

#### Detalles técnicos

**`python-jose` — CVE-2024-33663** ⚠️ Crítica
- **Descripción**: Algorithm confusion con claves ECDSA de OpenSSH. Un atacante puede forjar tokens JWT firmados con ECDSA sin conocer la clave privada.
- **Impacto**: Bypass de autenticación completo.
- **Afecta**: Semana 11 (JWT/OAuth2). Versión usada antes: `>=3.3.0`.
- **Fix**: `python-jose[cryptography]==3.5.0`

**`python-jose` — CVE-2024-33664** ⚠️ Moderada
- **Descripción**: DoS via "JWT bomb" — token JWE con contenido altamente comprimido que consume memoria al decodificar.
- **Impacto**: Denegación de servicio, paraliza el event loop en ASGI.
- **Fix**: `python-jose[cryptography]==3.5.0`

**`python-multipart` — CVE-2024-53981** ⚠️ Alta
- **Descripción**: DoS via boundary malformado en `multipart/form-data`. El parser emite un log por byte procesado antes del primer boundary, bloqueando el event loop.
- **Impacto**: Denegación de servicio remota sin autenticación (CVSS:AV:N/PR:N).
- **Fix**: `python-multipart==0.0.22`

**`python-multipart` — CVE-2026-24486** ⚠️ Alta
- **Descripción**: Path Traversal con configuración no default (`UPLOAD_DIR` + `UPLOAD_KEEP_FILENAME=True`). `os.path.join` descarta el directorio base si el filename empieza con `/`.
- **Impacto**: Escritura de archivos en rutas arbitrarias del servidor.
- **Fix**: `python-multipart==0.0.22`

**`jinja2` — CVE-2025-27516** ⚠️ Moderada
- **Descripción**: El filtro `|attr` permite escapar el sandbox de Jinja2 accediendo al método `.format` de strings, habilitando ejecución de código Python arbitrario.
- **Impacto**: RCE en aplicaciones que renderizan templates controlados por el usuario.
- **Fix**: `jinja2==3.1.6`

### Paquetes sin CVEs confirmados

Los siguientes paquetes fueron verificados sin vulnerabilidades activas en las versiones pineadas:

`fastapi==0.128.0` · `uvicorn==0.40.0` · `sqlalchemy==2.0.46` · `pydantic==2.12.0`
`pydantic-settings==2.6.0` · `passlib[bcrypt]==1.7.4` · `httpx==0.29.0`
`email-validator==2.2.0` · `pytest==8.4.0` · `pytest-asyncio==0.24.0/0.25.0`
`redis==5.2.0` · `slowapi==0.1.9` · `sse-starlette==2.0.0` · `structlog==24.4.0`
`ruff==0.8.0` · `mypy==1.13.0` · `prometheus-client==0.21.0`

> ⚠️ **Nota sobre `passlib`**: El paquete no tiene CVEs pero **no ha tenido releases desde 2020** (v1.7.4). Está en modo mantenimiento pasivo. Para nuevos proyectos de producción, considerar `bcrypt` directamente. En el contexto educativo del bootcamp es aceptable.

---

## 📋 Versiones pineadas — Mapa de referencia

Tabla de referencia para los instructores al crear contenido nuevo:

### Dependencias de producción

| Paquete | Versión pineada | Notas |
|---|---|---|
| `fastapi` | `0.128.0` | Versión base del bootcamp |
| `fastapi[standard]` | `0.128.0` | Con uvicorn incluido |
| `uvicorn` | `0.40.0` | |
| `uvicorn[standard]` | `0.40.0` | Con extras de performance |
| `sqlalchemy` | `2.0.46` | ORM async/sync |
| `pydantic` | `2.12.0` | |
| `pydantic[email]` | `2.10.0` | Con email-validator |
| `pydantic-settings` | `2.6.0` | Configuración con .env |
| `python-jose[cryptography]` | `3.5.0` | JWT — ⚠️ CVE fix |
| `passlib[bcrypt]` | `1.7.4` | Password hashing |
| `python-multipart` | `0.0.22` | Formularios — ⚠️ CVE fix |
| `jinja2` | `3.1.6` | Templates — ⚠️ CVE fix |
| `email-validator` | `2.2.0` | |
| `httpx` | `0.29.0` | HTTP client async |
| `redis` | `5.2.0` | |
| `slowapi` | `0.1.9` | Rate limiting |
| `sse-starlette` | `2.0.0` | Server-Sent Events |
| `structlog` | `24.4.0` | Logging estructurado |
| `prometheus-client` | `0.21.0` | Métricas |
| `prometheus-fastapi-instrumentator` | `7.0.0` | |
| `psutil` | `6.0.0` | |

### Dependencias de desarrollo y testing

| Paquete | Versión pineada |
|---|---|
| `pytest` | `8.4.0` |
| `pytest-asyncio` | `0.25.0` |
| `pytest-cov` | `6.0.0` |
| `pytest-mock` | `3.14.0` |
| `freezegun` | `1.4.0` |
| `respx` | `0.22.0` |
| `httpx` | `0.29.0` |
| `ruff` | `0.8.0` |
| `mypy` | `1.13.0` |

---

## 🔄 Procedimiento para actualizar versiones

Cuando se quiera actualizar una dependencia (por CVE nuevo o funcionalidad necesaria):

### 1. Verificar CVEs en la nueva versión

```bash
# Consultar base de datos GitHub Advisory
# https://github.com/advisories?query=ecosystem%3Apip+NOMBRE_PAQUETE

# O usar pip-audit puntualmente:
pip install pip-audit
echo "paquete==NUEVA_VERSION" > /tmp/check.txt
pip-audit --disable-pip -r /tmp/check.txt -s osv
```

### 2. Actualizar en todos los archivos

```bash
# Script de reemplazo masivo (desde la raíz del repo)
python3 -c "
import glob
OLD = '\"paquete==VERSION_VIEJA\"'
NEW = '\"paquete==VERSION_NUEVA\"'
for f in glob.glob('bootcamp/**/pyproject.toml', recursive=True):
    content = open(f).read()
    if OLD in content:
        open(f,'w').write(content.replace(OLD, NEW))
        print(f'Actualizado: {f}')
"
```

### 3. Verificar que no quedaron rangos abiertos

```bash
# Este comando debe retornar SOLO la línea de requires-python
grep -rh '".*>=' bootcamp --include="pyproject.toml" | grep -v "^#" | sort -u
```

### 4. Actualizar este documento

- Agregar la entrada en la tabla de "Versiones pineadas"
- Si hubo CVE, documentar en "Auditoría CVE" con fecha

---

## 🛡️ Próxima auditoría recomendada

- **Frecuencia**: cada 3 meses o ante cualquier aviso de seguridad
- **Herramienta**: `pip-audit` + revisión manual de GitHub Advisory
- **Próxima fecha sugerida**: Julio 2026
- **Responsable**: Mantenedor del bootcamp

---

_Documento creado: 04/04/2026_
_Última auditoría: 04/04/2026_
_Próxima auditoría: 01/07/2026_
