# 🛠️ Prácticas - Semana 02

## 📋 Descripción

Ejercicios prácticos para dominar Pydantic v2 y su integración con FastAPI.

---

## 📚 Ejercicios

| # | Ejercicio | Tema | Duración |
|---|-----------|------|----------|
| 01 | [BaseModel Básico](01-ejercicio-basemodel/) | Crear modelos, campos, configuración | 30 min |
| 02 | [Field y Restricciones](02-ejercicio-field/) | Field(), tipos especiales, constraints | 40 min |
| 03 | [Validadores](03-ejercicio-validadores/) | @field_validator, @model_validator | 45 min |
| 04 | [Integración FastAPI](04-ejercicio-integracion/) | Schemas CRUD, response_model | 45 min |

**Tiempo total estimado:** ~2.5 horas

---

## 🎯 Objetivos

Al completar estos ejercicios, podrás:

- ✅ Crear modelos Pydantic con campos requeridos y opcionales
- ✅ Configurar modelos con `model_config`
- ✅ Usar `Field()` para validaciones avanzadas
- ✅ Implementar validadores personalizados
- ✅ Integrar Pydantic con endpoints FastAPI

---

## 📝 Formato de Ejercicios

Cada ejercicio es un **tutorial guiado**. El código está comentado y debes:

1. **Leer** la explicación en el README
2. **Abrir** el archivo `starter/main.py`
3. **Descomentar** el código de cada paso
4. **Ejecutar** para verificar que funciona
5. **Experimentar** modificando valores

---

## 🚀 Cómo Ejecutar

### Con Docker (Recomendado)

```bash
cd ejercicio-XX-nombre/starter
docker compose up --build
```

### Sin Docker

```bash
cd ejercicio-XX-nombre/starter
uv sync
uv run python main.py
```

---

## ✅ Checklist de Progreso

- [ ] Ejercicio 01: BaseModel Básico
- [ ] Ejercicio 02: Field y Restricciones
- [ ] Ejercicio 03: Validadores
- [ ] Ejercicio 04: Integración FastAPI

---

[← Volver a Teoría](../1-teoria/) | [Ir al Proyecto →](../3-proyecto/)
