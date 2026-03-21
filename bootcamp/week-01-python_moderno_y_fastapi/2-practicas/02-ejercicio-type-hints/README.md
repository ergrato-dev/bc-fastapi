# 🏷️ Ejercicio 02: Type Hints en Práctica

## 🎯 Objetivo

Practicar el uso de type hints en Python para escribir código más claro y seguro.

**Duración estimada:** 30 minutos

---

## 📋 Requisitos Previos

- Haber completado el [Ejercicio 01](../01-ejercicio-setup/)
- Haber leído [Type Hints](../../1-teoria/03-type-hints.md)

---

## 📝 Instrucciones

### Paso 1: Tipos Básicos

Los type hints especifican qué tipo de dato espera y retorna una función.

**Abre `starter/main.py`** y descomenta la sección de tipos básicos:

```python
# Ejemplo de tipos básicos
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

---

### Paso 2: Tipos Compuestos

Las listas, diccionarios y otros contenedores también pueden tener tipos.

```python
# Python 3.9+ permite usar list, dict directamente
def process_numbers(numbers: list[int]) -> int:
    return sum(numbers)
```

---

### Paso 3: Tipos Opcionales

Cuando un valor puede ser `None`, usamos `| None` o `Optional`.

```python
# Python 3.10+ usa | para union types
def find_user(user_id: int) -> dict | None:
    # Puede retornar un dict o None
    pass
```

---

### Paso 4: Ejecutar y Verificar

```bash
# Ejecutar el script
docker compose exec api python src/main.py

# O si no tienes el contenedor corriendo:
docker compose run --rm api python src/main.py
```

---

## ✅ Checklist de Verificación

- [ ] Código ejecuta sin errores de tipo
- [ ] Entiendes la diferencia entre `list` y `list[str]`
- [ ] Sabes cuándo usar `| None`
- [ ] Puedes tipar funciones con múltiples parámetros

---

## 🔗 Navegación

[← Anterior: Setup](../01-ejercicio-setup/) | [Siguiente: Async →](../03-ejercicio-async/)
