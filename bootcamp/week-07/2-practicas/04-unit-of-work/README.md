# 🔨 Práctica 04: Unit of Work

## 🎯 Objetivo

Implementar el patrón Unit of Work para coordinar transacciones entre repositorios.

---

## 📋 Contexto

Cuando una operación involucra múltiples repositorios, necesitamos que todos los cambios sean atómicos (todo o nada).

---

## 📝 Instrucciones

### Paso 1: Revisar el problema

En `starter/problem.py` hay un ejemplo de transacción sin Unit of Work.

### Paso 2: Implementar UnitOfWork

En `starter/unit_of_work.py`, descomenta la clase `UnitOfWork`.

### Paso 3: Usar UoW en Service

En `starter/services.py`, descomenta el servicio que usa UoW.

### Paso 4: Probar

```bash
cd starter
uv run python main.py
```

---

## ✅ Resultado Esperado

- Unit of Work coordina múltiples repositorios
- Una sola sesión compartida
- Commit/rollback atómico
- Context manager para cleanup automático
