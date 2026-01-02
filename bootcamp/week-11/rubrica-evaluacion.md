# 📊 Rúbrica de Evaluación - Semana 11

## 🔐 Autenticación JWT y OAuth2

### Información General

| Aspecto | Detalle |
|---------|---------|
| **Semana** | 11 de 16 |
| **Tema** | Autenticación JWT y OAuth2 |
| **Nivel** | Avanzado |
| **Duración** | 6 horas |

---

## 📋 Criterios de Evaluación

### 1. Conocimiento Teórico (30%) 🧠

#### 1.1 Fundamentos de Autenticación (10%)

| Nivel | Criterio | Puntos |
|-------|----------|--------|
| **Excelente** | Explica diferencia autenticación/autorización con ejemplos, comprende amenazas comunes | 10 |
| **Bueno** | Diferencia los conceptos, conoce vectores de ataque básicos | 8 |
| **Suficiente** | Comprende autenticación básica, conoce conceptos generales | 6 |
| **Insuficiente** | No distingue autenticación de autorización | 0-5 |

#### 1.2 JSON Web Tokens (10%)

| Nivel | Criterio | Puntos |
|-------|----------|--------|
| **Excelente** | Explica header/payload/signature, algoritmos HS256/RS256, claims estándar y custom | 10 |
| **Bueno** | Comprende estructura JWT, sabe decodificar y verificar tokens | 8 |
| **Suficiente** | Entiende que JWT tiene partes, puede usar tokens | 6 |
| **Insuficiente** | No comprende estructura ni uso de JWT | 0-5 |

#### 1.3 OAuth2 y Seguridad (10%)

| Nivel | Criterio | Puntos |
|-------|----------|--------|
| **Excelente** | Domina Password Flow, conoce otros flows, entiende refresh tokens | 10 |
| **Bueno** | Implementa Password Flow, comprende ciclo de vida del token | 8 |
| **Suficiente** | Puede seguir flujo básico de autenticación | 6 |
| **Insuficiente** | No comprende OAuth2 | 0-5 |

---

### 2. Desempeño Práctico (40%) 💪

#### 2.1 Práctica 01: Password Hashing (10%)

| Nivel | Criterio | Puntos |
|-------|----------|--------|
| **Excelente** | Implementa bcrypt/argon2 correctamente, timing-safe comparison, salt automático | 10 |
| **Bueno** | Hashing funcional, verificación correcta | 8 |
| **Suficiente** | Hashing básico funciona | 6 |
| **Insuficiente** | No implementa hashing seguro | 0-5 |

#### 2.2 Práctica 02: JWT Tokens (10%)

| Nivel | Criterio | Puntos |
|-------|----------|--------|
| **Excelente** | Crea y valida JWT con python-jose, maneja expiración, claims custom | 10 |
| **Bueno** | Genera y verifica tokens correctamente | 8 |
| **Suficiente** | Tokens básicos funcionan | 6 |
| **Insuficiente** | No puede crear/validar JWT | 0-5 |

#### 2.3 Práctica 03: OAuth2 FastAPI (10%)

| Nivel | Criterio | Puntos |
|-------|----------|--------|
| **Excelente** | OAuth2PasswordBearer completo, token endpoint funcional, errores HTTP correctos | 10 |
| **Bueno** | Flujo OAuth2 funciona end-to-end | 8 |
| **Suficiente** | Login básico con token | 6 |
| **Insuficiente** | No implementa OAuth2 | 0-5 |

#### 2.4 Práctica 04: Protected Endpoints (10%)

| Nivel | Criterio | Puntos |
|-------|----------|--------|
| **Excelente** | Dependencias de seguridad, get_current_user, manejo de token inválido/expirado | 10 |
| **Bueno** | Endpoints protegidos funcionan, usuario actual disponible | 8 |
| **Suficiente** | Protección básica funciona | 6 |
| **Insuficiente** | No protege endpoints | 0-5 |

---

### 3. Producto Final - Proyecto (30%) 📦

#### 3.1 Funcionalidad (15%)

| Nivel | Criterio | Puntos |
|-------|----------|--------|
| **Excelente** | Registro, login, refresh, logout funcionan; tokens con expiración correcta | 15 |
| **Bueno** | Flujo completo funciona, refresh tokens implementados | 12 |
| **Suficiente** | Login y protección básica funcionan | 9 |
| **Insuficiente** | Sistema no funciona | 0-8 |

#### 3.2 Seguridad (10%)

| Nivel | Criterio | Puntos |
|-------|----------|--------|
| **Excelente** | Passwords hasheados, tokens firmados, headers seguros, no info sensible en logs | 10 |
| **Bueno** | Seguridad correcta en passwords y tokens | 8 |
| **Suficiente** | Hashing implementado | 6 |
| **Insuficiente** | Vulnerabilidades graves (passwords en texto plano, etc.) | 0-5 |

#### 3.3 Código y Documentación (5%)

| Nivel | Criterio | Puntos |
|-------|----------|--------|
| **Excelente** | Código limpio, documentado, tests de autenticación | 5 |
| **Bueno** | Código organizado, algunos tests | 4 |
| **Suficiente** | Código funcional | 3 |
| **Insuficiente** | Código desorganizado | 0-2 |

---

## 📈 Escala de Calificación

| Rango | Calificación | Descripción |
|-------|--------------|-------------|
| 90-100 | **Excelente** | Dominio completo del tema |
| 80-89 | **Muy Bueno** | Comprensión sólida con detalles menores |
| 70-79 | **Bueno** | Cumple objetivos principales |
| 60-69 | **Suficiente** | Mínimo aceptable |
| < 60 | **Insuficiente** | Requiere refuerzo |

---

## 🎯 Competencias Evaluadas

### Técnicas

- Implementación de OAuth2 Password Flow
- Generación y validación de JWT
- Hashing seguro de contraseñas
- Protección de endpoints con dependencias
- Manejo de refresh tokens

### Transversales

- Pensamiento en seguridad
- Atención al detalle (claves, expiración, etc.)
- Buenas prácticas de desarrollo seguro

---

## ⚠️ Penalizaciones

| Situación | Penalización |
|-----------|--------------|
| Contraseñas en texto plano | -20 puntos |
| Secret key hardcodeada en código | -10 puntos |
| Tokens sin expiración | -10 puntos |
| No validar token en endpoints protegidos | -15 puntos |
| Exponer información sensible en errores | -10 puntos |
| Entrega tardía (por día) | -5 puntos |
| Plagio | **Descalificación** |

---

## 📝 Notas Adicionales

- La seguridad es crítica en esta semana
- Nunca almacenar contraseñas en texto plano
- Siempre usar HTTPS en producción (aunque no en desarrollo local)
- Los tokens deben tener tiempos de expiración razonables
- El código debe manejar todos los casos de error

---

## 🔗 Referencias

- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
- [FastAPI Security Tutorial](https://fastapi.tiangolo.com/tutorial/security/)
- [JWT Best Practices](https://auth0.com/blog/jwt-security-best-practices/)
