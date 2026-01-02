# 📖 Glosario - Semana 11: Autenticación JWT y OAuth2

## A

### Access Token
Token de corta duración (15-30 min) que autoriza el acceso a recursos protegidos. Se envía en cada request al API.

### Algorithm (JWT)
Método criptográfico usado para firmar el JWT. Los más comunes son HS256 (simétrico) y RS256 (asimétrico).

### Authentication (AuthN)
Proceso de verificar la identidad de un usuario. Responde a la pregunta: "¿Quién eres?"

### Authorization (AuthZ)
Proceso de verificar los permisos de un usuario. Responde a la pregunta: "¿Qué puedes hacer?"

---

## B

### Bearer Token
Tipo de token que se envía en el header `Authorization: Bearer <token>`. Quien lo posee (bearer) tiene acceso.

### bcrypt
Algoritmo de hashing diseñado específicamente para passwords. Incluye salt automático y es deliberadamente lento.

---

## C

### Claim
Pieza de información dentro del payload de un JWT. Ejemplos: `sub`, `exp`, `iat`, `role`.

### Credentials
Par de identificador y secreto (email/password) usados para autenticación.

### CryptContext
Clase de passlib que maneja múltiples algoritmos de hashing y facilita la migración entre ellos.

---

## D

### Decode
Proceso de extraer el payload de un JWT verificando su firma.

### Dependency (FastAPI)
Función inyectable que proporciona valores a endpoints. Usada para autenticación con `Depends()`.

---

## E

### Expiration (exp)
Claim estándar de JWT que indica cuándo expira el token. Después de este tiempo, el token es inválido.

---

## F

### Form Data
Formato de envío de datos (`application/x-www-form-urlencoded`) requerido por OAuth2 para el endpoint de token.

---

## H

### Hash
Valor de longitud fija generado a partir de un input. Es unidireccional (no se puede revertir).

### Header (JWT)
Primera parte del JWT que contiene el tipo de token y el algoritmo de firma.

### HS256
HMAC con SHA-256. Algoritmo simétrico donde la misma clave firma y verifica.

---

## I

### Issued At (iat)
Claim de JWT que indica cuándo fue creado el token.

---

## J

### JWT (JSON Web Token)
Estándar abierto (RFC 7519) para transmitir información de forma segura entre partes como un objeto JSON firmado.

### JWTError
Excepción de python-jose lanzada cuando un token es inválido, expirado o tiene firma incorrecta.

---

## O

### OAuth2
Framework de autorización (RFC 6749) que permite a aplicaciones obtener acceso limitado a cuentas de usuario.

### OAuth2PasswordBearer
Clase de FastAPI que extrae el token del header Authorization y se integra con Swagger UI.

### OAuth2PasswordRequestForm
Clase de FastAPI que parsea las credenciales enviadas como form data según especificación OAuth2.

---

## P

### Payload (JWT)
Segunda parte del JWT que contiene los claims (datos). Está codificado en Base64 pero NO encriptado.

### passlib
Librería Python para hashing de passwords que soporta múltiples algoritmos y maneja migraciones.

### Password Flow
Flujo OAuth2 donde el usuario proporciona credenciales directamente a la aplicación (Resource Owner Password Credentials).

### python-jose
Librería Python para crear y verificar JWTs. Soporta múltiples backends criptográficos.

---

## R

### RBAC (Role-Based Access Control)
Modelo de autorización donde los permisos se asignan a roles, y los roles se asignan a usuarios.

### Refresh Token
Token de larga duración (días/semanas) usado exclusivamente para obtener nuevos access tokens sin re-autenticar.

### RS256
RSA con SHA-256. Algoritmo asimétrico con clave privada para firmar y pública para verificar.

---

## S

### Salt
Valor aleatorio añadido al password antes de hashear. Previene ataques con rainbow tables.

### Secret Key
Clave secreta usada para firmar JWTs con algoritmos simétricos (HS256). Debe mantenerse confidencial.

### Signature (JWT)
Tercera parte del JWT. Resultado de firmar header+payload con el algoritmo especificado.

### Subject (sub)
Claim estándar de JWT que identifica al sujeto del token (generalmente el ID o email del usuario).

---

## T

### Token
Cadena que representa una autorización otorgada. Puede ser opaco o auto-contenido (JWT).

### Token Blacklist
Lista de tokens revocados que aún no han expirado. Requiere almacenamiento adicional.

### Token Rotation
Práctica de invalidar el refresh token anterior al generar uno nuevo, mejorando la seguridad.

### tokenUrl
Parámetro de OAuth2PasswordBearer que indica la ruta del endpoint de login para Swagger UI.

---

## V

### Verify
Proceso de comprobar que un password coincide con su hash almacenado, o que la firma de un JWT es válida.

---

## W

### WWW-Authenticate
Header HTTP retornado con respuestas 401 que indica el esquema de autenticación requerido (`Bearer`).

---

## Símbolos y Abreviaturas

| Símbolo | Significado |
|---------|-------------|
| AuthN | Authentication |
| AuthZ | Authorization |
| JWT | JSON Web Token |
| RBAC | Role-Based Access Control |
| MFA | Multi-Factor Authentication |
| OIDC | OpenID Connect |

---

*Última actualización: Enero 2026*
