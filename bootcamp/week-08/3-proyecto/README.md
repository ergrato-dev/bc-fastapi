# 🛒 Proyecto: E-Commerce API

## 📋 Descripción

Construirás una **API de E-Commerce completa** aplicando arquitectura en capas (MVC). El proyecto consolida todos los conceptos de la semana: estructura por capas, DTOs, Mappers, manejo de errores centralizado y flujo completo de datos.

---

## 🎯 Objetivos

- Implementar arquitectura en capas completa
- Crear DTOs específicos por operación
- Usar Mappers para conversiones
- Implementar excepciones personalizadas
- Configurar exception handlers globales
- Crear flujos de negocio complejos

---

## 🏗️ Arquitectura

```
┌─────────────────────────────────────────────────────────────┐
│                    PRESENTATION LAYER                        │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐           │
│  │ Users   │ │Products │ │ Orders  │ │Categories│           │
│  │ Router  │ │ Router  │ │ Router  │ │ Router  │           │
│  └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘           │
└───────┼──────────┼──────────┼──────────┼───────────────────┘
        │          │          │          │
        ▼          ▼          ▼          ▼
┌─────────────────────────────────────────────────────────────┐
│                    APPLICATION LAYER                         │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐           │
│  │ User    │ │Product  │ │ Order   │ │Category │           │
│  │ Service │ │ Service │ │ Service │ │ Service │           │
│  └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘           │
└───────┼──────────┼──────────┼──────────┼───────────────────┘
        │          │          │          │
        ▼          ▼          ▼          ▼
┌─────────────────────────────────────────────────────────────┐
│                    DATA ACCESS LAYER                         │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐           │
│  │ User    │ │Product  │ │ Order   │ │Category │           │
│  │  Repo   │ │  Repo   │ │  Repo   │ │  Repo   │           │
│  └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘           │
└───────┼──────────┼──────────┼──────────┼───────────────────┘
        │          │          │          │
        └──────────┴──────────┴──────────┘
                       │
                       ▼
                 ┌──────────┐
                 │ Database │
                 │ (SQLite) │
                 └──────────┘
```

---

## 📁 Estructura del Proyecto

```
starter/
├── main.py                      # Punto de entrada
├── config.py                    # Configuración
├── database.py                  # Conexión DB
│
├── models/                      # Entities (SQLAlchemy)
│   ├── __init__.py
│   ├── user.py
│   ├── category.py
│   ├── product.py
│   └── order.py
│
├── schemas/                     # DTOs (Pydantic)
│   ├── __init__.py
│   ├── user.py
│   ├── category.py
│   ├── product.py
│   └── order.py
│
├── mappers/                     # Conversiones
│   ├── __init__.py
│   ├── user.py
│   ├── product.py
│   └── order.py
│
├── repositories/                # Data Access
│   ├── __init__.py
│   ├── base.py
│   ├── user.py
│   ├── category.py
│   ├── product.py
│   └── order.py
│
├── services/                    # Business Logic
│   ├── __init__.py
│   ├── user.py
│   ├── category.py
│   ├── product.py
│   └── order.py
│
├── routers/                     # Endpoints
│   ├── __init__.py
│   ├── users.py
│   ├── categories.py
│   ├── products.py
│   └── orders.py
│
├── exceptions/                  # Custom Exceptions
│   ├── __init__.py
│   ├── base.py
│   ├── user.py
│   ├── category.py
│   ├── product.py
│   └── order.py
│
├── handlers/                    # Exception Handlers
│   ├── __init__.py
│   └── exception_handlers.py
│
└── dependencies.py              # Dependency Injection
```

---

## 📊 Modelos de Datos

### User
- `id`, `email`, `name`, `password_hash`, `is_active`, `created_at`

### Category
- `id`, `name`, `description`, `is_active`, `created_at`

### Product
- `id`, `name`, `sku`, `description`, `price`, `stock`, `category_id`, `is_active`, `created_at`

### Order
- `id`, `user_id`, `status`, `subtotal`, `tax`, `shipping_cost`, `total`, `shipping_address`, `created_at`

### OrderItem
- `id`, `order_id`, `product_id`, `product_name`, `quantity`, `unit_price`, `subtotal`

---

## 🔧 Endpoints Requeridos

### Users
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/users/` | Crear usuario |
| GET | `/users/` | Listar usuarios |
| GET | `/users/{id}` | Obtener usuario |

### Categories
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/categories/` | Crear categoría |
| GET | `/categories/` | Listar categorías |
| GET | `/categories/{id}` | Obtener categoría |
| PATCH | `/categories/{id}` | Actualizar categoría |
| DELETE | `/categories/{id}` | Eliminar categoría |

### Products
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/products/` | Crear producto |
| GET | `/products/` | Listar productos |
| GET | `/products/{id}` | Obtener producto |
| PATCH | `/products/{id}` | Actualizar producto |
| DELETE | `/products/{id}` | Eliminar producto |
| GET | `/products/category/{id}` | Productos por categoría |

### Orders
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/orders/` | Crear pedido |
| GET | `/orders/{id}` | Obtener pedido |
| GET | `/orders/user/{id}` | Pedidos de usuario |
| PATCH | `/orders/{id}/status` | Cambiar estado |
| PATCH | `/orders/{id}/cancel` | Cancelar pedido |

---

## ✅ Requisitos

### Arquitectura
- [ ] Separación clara en 3 capas
- [ ] Routers solo manejan HTTP
- [ ] Services contienen lógica de negocio
- [ ] Repositories solo acceso a datos

### DTOs
- [ ] Create, Update y Response por entidad
- [ ] Campos sensibles no expuestos (password_hash)
- [ ] Validaciones con Pydantic Field

### Errores
- [ ] Excepciones personalizadas por dominio
- [ ] Handlers globales registrados
- [ ] Respuestas de error consistentes

### Negocio
- [ ] Crear pedido reduce stock
- [ ] Validar stock antes de crear pedido
- [ ] Cancelar pedido restaura stock
- [ ] No eliminar categoría con productos

---

## 🚀 Instrucciones

1. **Completa los TODOs** en cada archivo
2. Sigue el orden: models → schemas → repositories → services → routers
3. Ejecuta con `uvicorn main:app --reload`
4. Prueba todos los endpoints en `/docs`

---

## 📋 Criterios de Evaluación

| Criterio | Puntos |
|----------|--------|
| Estructura de capas correcta | 25% |
| DTOs y Mappers implementados | 25% |
| Manejo de errores centralizado | 25% |
| Flujos de negocio funcionando | 25% |

---

## 💡 Tips

- Usa las prácticas como referencia
- Empieza por el dominio más simple (Category)
- Prueba cada capa antes de pasar a la siguiente
- Los exception handlers simplifican mucho el código
