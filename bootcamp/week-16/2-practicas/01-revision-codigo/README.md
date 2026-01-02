# 🔍 Práctica 01: Revisión de Código

## 📋 Descripción

En esta práctica aprenderás a realizar **code reviews** efectivos de tu propio proyecto y el de otros. La revisión de código es una habilidad esencial para cualquier desarrollador profesional.

---

## 🎯 Objetivos

1. Aplicar checklist de code review
2. Identificar code smells comunes
3. Usar herramientas de análisis estático
4. Mejorar la calidad del código

---

## ⏱️ Duración

~45 minutos

---

## 📚 Conceptos Clave

### ¿Qué es Code Review?

El code review es el proceso de examinar código escrito por ti u otros desarrolladores para:
- Encontrar bugs antes de producción
- Mejorar la calidad y legibilidad
- Compartir conocimiento en el equipo
- Mantener consistencia en el codebase

### Checklist de Review

```markdown
## Checklist de Code Review

### Funcionalidad
- [ ] ¿El código hace lo que debería?
- [ ] ¿Maneja casos edge correctamente?
- [ ] ¿Los errores se manejan apropiadamente?

### Legibilidad
- [ ] ¿Los nombres son descriptivos?
- [ ] ¿El código es fácil de entender?
- [ ] ¿Los comentarios son útiles (no obvios)?

### Arquitectura
- [ ] ¿Sigue los patrones del proyecto?
- [ ] ¿Las responsabilidades están separadas?
- [ ] ¿Es fácil de testear?

### Seguridad
- [ ] ¿Los inputs están validados?
- [ ] ¿No hay secrets hardcodeados?
- [ ] ¿SQL injection prevenido?

### Performance
- [ ] ¿Hay queries N+1?
- [ ] ¿Se usa paginación donde corresponde?
- [ ] ¿Operaciones costosas en background?

### Testing
- [ ] ¿Hay tests para la nueva funcionalidad?
- [ ] ¿Los tests son significativos?
- [ ] ¿Coverage adecuado?
```

---

## 🛠️ Paso a Paso

### Paso 1: Configurar Herramientas de Análisis

Abre `starter/setup_tools.py` y sigue las instrucciones para configurar las herramientas de análisis estático.

### Paso 2: Ejecutar Análisis Estático

Usa los comandos en `starter/run_analysis.sh` para analizar tu proyecto.

### Paso 3: Revisar Code Smells

Abre `starter/code_smells.py` para ver ejemplos de code smells comunes y cómo refactorizarlos.

### Paso 4: Self-Review de tu Proyecto

Usa el checklist en `starter/self_review_checklist.md` para revisar tu proyecto final.

---

## 📁 Archivos

```
01-revision-codigo/
├── README.md
└── starter/
    ├── setup_tools.py
    ├── run_analysis.sh
    ├── code_smells.py
    └── self_review_checklist.md
```

---

## ✅ Criterios de Éxito

- [ ] Herramientas de análisis configuradas
- [ ] Análisis ejecutado sin errores críticos
- [ ] Code smells identificados y documentados
- [ ] Self-review completado con al menos 5 mejoras identificadas
