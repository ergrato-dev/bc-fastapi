# 🔒 Práctica 01: Password Hashing

## 🎯 Objetivos

- Implementar hashing seguro con passlib y bcrypt
- Verificar contraseñas de forma segura
- Validar fortaleza de contraseñas

---

## 📋 Instrucciones

En esta práctica implementarás las funciones de seguridad para contraseñas.

### Paso 1: Configurar el Proyecto

Abre `starter/` y revisa la estructura:

```
starter/
├── pyproject.toml
├── src/
│   ├── __init__.py
│   └── security/
│       ├── __init__.py
│       └── password.py    # ← Completar aquí
└── tests/
    └── test_password.py
```

### Paso 2: Instalar Dependencias

```bash
cd starter
uv sync
```

### Paso 3: Implementar Hashing

Abre `src/security/password.py` y descomenta el código según las instrucciones.

### Paso 4: Ejecutar Tests

```bash
uv run pytest tests/test_password.py -v
```

---

## ✅ Criterios de Éxito

- [ ] `hash_password()` genera hashes bcrypt válidos
- [ ] `verify_password()` retorna True para password correcto
- [ ] `verify_password()` retorna False para password incorrecto
- [ ] `validate_password_strength()` detecta passwords débiles
- [ ] Todos los tests pasan
