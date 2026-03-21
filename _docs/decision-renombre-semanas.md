# 📋 Decisión: Renombre de Carpetas de Semanas

**Fecha**: Marzo 2026  
**Estado**: ✅ Implementado  
**Alcance**: Todo el repositorio

---

## Contexto

Las carpetas de semanas usaban el esquema `week-XX` (ej. `week-01`, `week-02`), lo que no dejaba claro el contenido de cada semana sin abrir el README.

## Decisión

Se adopta el esquema `week-XX-tema_principal` extrayendo el tema del encabezado H1 del README de cada semana.

### Tabla de renombres

| Nombre anterior | Nombre nuevo |
|-----------------|--------------|
| `week-01` | `week-01-python_moderno_y_fastapi` |
| `week-02` | `week-02-pydantic_v2_validacion_datos` |
| `week-03` | `week-03-rutas_parametros_y_query_strings` |
| `week-04` | `week-04-responses_y_manejo_de_errores` |
| `week-05` | `week-05-sqlalchemy_orm_introduccion` |
| `week-06` | `week-06-relaciones_sqlalchemy_service_layer` |
| `week-07` | `week-07-repository_pattern` |
| `week-08` | `week-08-arquitectura_en_capas_completa` |
| `week-09` | `week-09-ports_and_adapters` |
| `week-10` | `week-10-arquitectura_hexagonal_completa` |
| `week-11` | `week-11-autenticacion_jwt_y_oauth2` |
| `week-12` | `week-12-testing_pytest` |
| `week-13` | `week-13-websockets_y_server_sent_events` |
| `week-14` | `week-14-rate_limiting_seguridad_logging` |
| `week-15` | `week-15-docker_cicd_produccion` |
| `week-16` | `week-16-proyecto_final` |

## Convención para nuevas semanas

```
week-XX-tema_en_snake_case
```

- El tema se extrae **exclusivamente del título H1 del README.md** de la semana.
- Usar `snake_case` en minúsculas.
- Sin caracteres especiales ni tildes.
- Separar palabras con guión bajo `_`.

## Cambios realizados

1. **Carpetas renombradas**: `bootcamp/week-XX` → `bootcamp/week-XX-tema_principal`
2. **Archivos actualizados** (enlaces relativos corregidos):
   - `README.md` (raíz)
   - `README_EN.md` (raíz)
   - `_docs/README.md`
   - `.github/copilot-instructions.md`
   - Todos los `bootcamp/week-XX-*/README.md` (navegación entre semanas)
   - `bootcamp/week-02-*/5-glosario/README.md`
   - `bootcamp/week-16-*/1-teoria/01-proyecto-final-guia.md`
   - `bootcamp/week-XX-*/2-practicas/README.md` (enlaces de retorno)
   - `bootcamp/week-XX-*/4-recursos/README.md` (enlaces de retorno)
   - `bootcamp/week-XX-*/5-glosario/README.md` (enlaces de retorno)
3. **No modificados** (intencionalmente):
   - `CONTRIBUTING.md`: ejemplos de mensajes de commit (`feat(week-03):`) — son convenciones de texto, no rutas de archivos.
   - `_scripts/README.md`: ejemplo de commit en documentación de scripts.
   - `.github/ISSUE_TEMPLATE/*.md`: ejemplos de texto `[ej. week-03]`.
   - `bootcamp/week-09-*/rubrica-evaluacion.md`: `week-09-nombre-apellido/` es una convención de nombre de entrega del estudiante, no una ruta del repositorio.

## Justificación

- **Navegabilidad**: El nombre de carpeta describe su contenido de forma inmediata.
- **Consistencia**: Sigue el patrón ya establecido en el copilot-instructions (`week-01-python_moderno_y_fastapi`).
- **Escalabilidad**: Facilita futuras búsquedas por tema sin abrir archivos.
