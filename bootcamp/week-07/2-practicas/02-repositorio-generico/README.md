# 🔨 Práctica 02: Repositorio Genérico

## 🎯 Objetivo

Implementar un `BaseRepository` genérico para evitar duplicación de código CRUD.

---

## 📋 Contexto

Cuando tienes múltiples entidades, el código CRUD se repite. Un repositorio genérico con Python Generics resuelve esto.

---

## 📝 Instrucciones

### Paso 1: Entender el problema

Revisa `starter/repositories_before.py` para ver la duplicación de código.

### Paso 2: Crear BaseRepository

En `starter/base_repository.py`, descomenta la implementación de `BaseRepository`.

### Paso 3: Crear repositorios específicos

En `starter/repositories.py`, descomenta los repositorios que heredan de `BaseRepository`.

### Paso 4: Probar

```bash
cd starter
uv run python main.py
```

---

## ✅ Resultado Esperado

- `BaseRepository` con métodos genéricos CRUD
- `ProductRepository` y `CategoryRepository` heredando
- Métodos específicos en cada repositorio
- Sin duplicación de código
