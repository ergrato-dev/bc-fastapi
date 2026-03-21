# 🔄 Ejercicio 03: Programación Asíncrona

## 🎯 Objetivo

Practicar la programación asíncrona con `async/await` en Python.

**Duración estimada:** 30 minutos

---

## 📋 Requisitos Previos

- Haber completado los ejercicios anteriores
- Haber leído [Async/Await](../../1-teoria/04-async-await.md)

---

## 📝 Instrucciones

### Paso 1: Tu Primera Coroutine

Una coroutine es una función definida con `async def`:

```python
async def my_coroutine():
    return "Hello, async!"
```

**Abre `starter/main.py`** y descomenta el Paso 1.

---

### Paso 2: Usando await

`await` pausa la coroutine hasta que la operación termine:

```python
async def main():
    result = await my_coroutine()
    print(result)
```

---

### Paso 3: Tareas Concurrentes

`asyncio.gather()` ejecuta múltiples coroutines en paralelo:

```python
results = await asyncio.gather(task1(), task2(), task3())
```

---

### Paso 4: Ejecutar

```bash
# Ejecutar el script
docker compose run --rm api python src/main.py
```

---

## ✅ Checklist de Verificación

- [ ] Entiendes la diferencia entre `def` y `async def`
- [ ] Sabes cuándo usar `await`
- [ ] Puedes ejecutar tareas en paralelo con `asyncio.gather()`
- [ ] Comprendes por qué async es más eficiente para I/O

---

## 🔗 Navegación

[← Anterior: Type Hints](../02-ejercicio-type-hints/) | [Siguiente: Primera API →](../04-ejercicio-primera-api/)
