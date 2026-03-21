# 🚀 Proyecto Semana 04: API con Responses y Manejo de Errores

## 🏛️ Tu Dominio Asignado

**Dominio**: `[El instructor te asignará tu dominio único]`

> ⚠️ **IMPORTANTE**: Cada aprendiz trabaja sobre un dominio diferente.

### 💡 Ejemplo Genérico de Referencia

> Los ejemplos usan **"Warehouse"** (Almacén) que NO está en el pool.
> **Debes adaptar TODO a tu dominio asignado.**

| Concepto | Ejemplo Genérico | Adapta a tu Dominio |
|----------|-----------------|---------------------|
| Main Entity | `StockTransfer` | `{YourEntity}` |
| States | `pending, in_transit, completed, cancelled` | `{your_states}` |
| Actions | `dispatch, receive, cancel` | `{your_actions}` |

---

## 🎯 Objetivo

Construir una **API REST completa** aplicando responses, status codes, manejo de errores y documentación OpenAPI.

---

## 📦 Requisitos Funcionales (Adapta a tu Dominio)

### Entity with States (Mínimo 10 campos)

```python
# Ejemplo genérico (Warehouse - StockTransfer)
class TransferStatus(str, Enum):
    PENDING = "pending"
    IN_TRANSIT = "in_transit"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

StockTransfer:
    id: int
    transfer_code: str      # Unique: TRF-YYYYMMDD-XXX
    origin_zone: str
    destination_zone: str
    item_id: int
    quantity: int
    status: TransferStatus
    requested_by: str
    notes: str | None
    created_at: datetime
    dispatched_at: datetime | None
    completed_at: datetime | None
```

### State Transitions

```python
# Ejemplo genérico (Warehouse)
# pending → in_transit (dispatch)
# in_transit → completed (receive)
# pending/in_transit → cancelled (cancel)

@app.post("/transfers/{id}/dispatch")
async def dispatch_transfer(id: int) -> TransferResponse:
    # Cambiar de pending → in_transit
    ...

@app.post("/transfers/{id}/receive")
async def receive_transfer(id: int) -> TransferResponse:
    # Cambiar de in_transit → completed
    ...
```

### Response Models

```python
# Ejemplo genérico
class TransferResponse(BaseModel):
    """Response sin datos sensibles"""
    id: int
    transfer_code: str
    status: TransferStatus
    # NO incluir: requested_by (interno)

class TransferDetailResponse(TransferResponse):
    """Response completo para admin"""
    requested_by: str
    notes: str | None
```

### Error Handling

```python
class TransferNotFoundError(HTTPException):
    def __init__(self, transfer_id: int):
        super().__init__(
            status_code=404,
            detail=f"Transfer {transfer_id} not found"
        )

class InvalidTransitionError(HTTPException):
    def __init__(self, current: str, target: str):
        super().__init__(
            status_code=400,
            detail=f"Cannot transition from {current} to {target}"
        )
```

---

## 🗂️ Estructura del Proyecto

```
starter/
├── main.py
├── models.py
├── schemas/
│   ├── request.py
│   └── response.py
├── exceptions.py
├── routers/
│   └── transfers.py
├── pyproject.toml
├── Dockerfile
└── docker-compose.yml
```

---

## ✅ Criterios de Evaluación

| Criterio | Puntos |
|----------|--------|
| **Funcionalidad** (40%) | |
| CRUD + transiciones de estado | 15 |
| Status codes correctos | 15 |
| Manejo de errores consistente | 10 |
| **Adaptación al Dominio** (35%) | |
| Estados coherentes con negocio | 12 |
| Transiciones lógicas | 13 |
| Originalidad (no copia ejemplo) | 10 |
| **Calidad del Código** (25%) | |
| Response models bien diseñados | 10 |
| Documentación OpenAPI completa | 10 |
| Código limpio | 5 |
| **Total** | **100** |

---

## ⚠️ Política Anticopia

- ❌ **No copies** el ejemplo genérico "StockTransfer"
- ✅ **Diseña** estados específicos de tu dominio
- ✅ **Crea** transiciones lógicas para tu negocio

---

## 📚 Recursos

- [Response Model](https://fastapi.tiangolo.com/tutorial/response-model/)
- [Handling Errors](https://fastapi.tiangolo.com/tutorial/handling-errors/)
- [Pool de Dominios](../../../_apprentices-only/dominios/POOL-DOMINIOS.md)

---

**Tiempo estimado:** 2-3 horas

[← Volver a Prácticas](../2-practicas/) | [Recursos →](../4-recursos/)
