# 🎫 Práctica 02: JWT Tokens

## 🎯 Objetivos

- Crear JSON Web Tokens con python-jose
- Validar y decodificar JWT
- Manejar expiración y claims personalizados

---

## 📋 Instrucciones

En esta práctica implementarás funciones para crear y validar JWT.

### Paso 1: Revisar la Estructura

```
starter/
├── pyproject.toml
├── src/
│   ├── __init__.py
│   └── security/
│       ├── __init__.py
│       └── jwt.py    # ← Completar aquí
└── tests/
    └── test_jwt.py
```

### Paso 2: Instalar Dependencias

```bash
cd starter
uv sync
```

### Paso 3: Implementar JWT

Abre `src/security/jwt.py` y descomenta el código según las instrucciones.

### Paso 4: Ejecutar Tests

```bash
uv run pytest tests/test_jwt.py -v
```

---

## ✅ Criterios de Éxito

- [ ] `create_access_token()` genera JWT válidos
- [ ] `decode_token()` decodifica tokens correctamente
- [ ] Tokens expirados lanzan excepción
- [ ] Claims personalizados funcionan
- [ ] Todos los tests pasan
