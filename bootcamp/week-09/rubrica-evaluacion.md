# 📋 Rúbrica de Evaluación - Semana 09

## Ports & Adapters (Inversión de Dependencias)

---

## 📊 Distribución de Puntuación

| Tipo de Evidencia | Porcentaje | Puntos |
|-------------------|------------|--------|
| 🧠 Conocimiento | 30% | 30 pts |
| 💪 Desempeño | 40% | 40 pts |
| 📦 Producto | 30% | 30 pts |
| **Total** | **100%** | **100 pts** |

---

## 🧠 Evidencia de Conocimiento (30 pts)

### Cuestionario Teórico

| Criterio | Excelente (10) | Bueno (7) | Regular (5) | Insuficiente (0-3) |
|----------|----------------|-----------|-------------|-------------------|
| **Patrón Ports & Adapters** | Explica correctamente el patrón, sus componentes y beneficios | Entiende el patrón pero confunde algunos términos | Conocimiento básico incompleto | No comprende el patrón |
| **Protocols en Python** | Domina Protocols, typing, runtime_checkable | Usa Protocols correctamente | Confusión entre Protocol y ABC | No sabe usar Protocols |
| **Principio DIP** | Explica DIP y lo aplica en ejemplos | Entiende DIP pero aplicación limitada | Confunde inversión con inyección | No comprende DIP |

### Preguntas de Evaluación

1. **¿Cuál es la diferencia entre un Port y un Adapter?**
   - Port: interfaz/contrato que define qué operaciones necesita el dominio
   - Adapter: implementación concreta que satisface el contrato del port

2. **¿Por qué usar Protocol en lugar de ABC (Abstract Base Class)?**
   - Protocol permite duck typing estructural (no requiere herencia)
   - Más flexible para testing y mockeo
   - Compatible con clases existentes sin modificarlas

3. **Explica el Principio de Inversión de Dependencias**
   - Los módulos de alto nivel no deben depender de módulos de bajo nivel
   - Ambos deben depender de abstracciones
   - Las abstracciones no deben depender de detalles

---

## 💪 Evidencia de Desempeño (40 pts)

### Práctica 01: Definir Ports (10 pts)

| Criterio | Puntos | Descripción |
|----------|--------|-------------|
| Sintaxis Protocol correcta | 3 | Usa `Protocol` de `typing` correctamente |
| Métodos bien definidos | 3 | Type hints completos, nombres descriptivos |
| Documentación | 2 | Docstrings explicando el contrato |
| Organización | 2 | Estructura de archivos clara |

```python
# ✅ Ejemplo correcto
from typing import Protocol

class NotificationSender(Protocol):
    """Port para envío de notificaciones."""
    
    async def send(
        self, 
        recipient: str, 
        message: str,
        subject: str | None = None
    ) -> bool:
        """
        Envía una notificación.
        
        Args:
            recipient: Destinatario
            message: Contenido del mensaje
            subject: Asunto opcional
            
        Returns:
            True si se envió correctamente
        """
        ...
```

### Práctica 02: Crear Adapters (10 pts)

| Criterio | Puntos | Descripción |
|----------|--------|-------------|
| Implementación completa | 4 | Todos los métodos del Protocol |
| Sin herencia explícita | 2 | No usa `class X(Protocol)` |
| Manejo de errores | 2 | Excepciones apropiadas |
| Configuración externa | 2 | Usa inyección para config |

```python
# ✅ Ejemplo correcto
class EmailAdapter:
    """Adapter para envío de emails via SMTP."""
    
    def __init__(self, smtp_config: SMTPConfig):
        self._config = smtp_config
    
    async def send(
        self,
        recipient: str,
        message: str,
        subject: str | None = None
    ) -> bool:
        # Implementación real
        try:
            await self._send_email(recipient, subject or "Notificación", message)
            return True
        except SMTPError as e:
            logger.error(f"Error enviando email: {e}")
            return False
```

### Práctica 03: Inyección de Dependencias (10 pts)

| Criterio | Puntos | Descripción |
|----------|--------|-------------|
| Factory functions | 3 | Crea adapters correctamente |
| FastAPI Depends | 3 | Integración con el framework |
| Configuración por entorno | 2 | Dev/Test/Prod diferentes |
| Service recibe ports | 2 | No instancia adapters internamente |

```python
# ✅ Ejemplo correcto
def get_notification_sender() -> NotificationSender:
    """Factory que retorna el adapter según configuración."""
    if settings.NOTIFICATION_PROVIDER == "email":
        return EmailAdapter(settings.smtp_config)
    elif settings.NOTIFICATION_PROVIDER == "sms":
        return SMSAdapter(settings.sms_config)
    else:
        return ConsoleAdapter()  # Para desarrollo

class NotificationService:
    def __init__(self, sender: NotificationSender):
        self._sender = sender  # Port, no adapter específico
```

### Práctica 04: Testing con Mocks (10 pts)

| Criterio | Puntos | Descripción |
|----------|--------|-------------|
| Fake adapters | 4 | Implementaciones para testing |
| Tests unitarios | 3 | Service testeado con fakes |
| Verificación de llamadas | 2 | Spy pattern cuando necesario |
| Cobertura de casos | 1 | Happy path + error cases |

```python
# ✅ Ejemplo correcto
class FakeNotificationSender:
    """Fake adapter para testing."""
    
    def __init__(self):
        self.sent_messages: list[tuple[str, str, str | None]] = []
        self.should_fail = False
    
    async def send(
        self,
        recipient: str,
        message: str,
        subject: str | None = None
    ) -> bool:
        if self.should_fail:
            return False
        self.sent_messages.append((recipient, message, subject))
        return True

@pytest.mark.asyncio
async def test_notification_service_sends_message():
    # Arrange
    fake_sender = FakeNotificationSender()
    service = NotificationService(sender=fake_sender)
    
    # Act
    result = await service.notify_user("user@test.com", "Hello!")
    
    # Assert
    assert result is True
    assert len(fake_sender.sent_messages) == 1
    assert fake_sender.sent_messages[0][0] == "user@test.com"
```

---

## 📦 Evidencia de Producto (30 pts)

### Proyecto: Notification Service

Sistema de notificaciones multi-canal con arquitectura Ports & Adapters.

#### Criterios de Evaluación

| Criterio | Excelente (6) | Bueno (4) | Regular (2) | Insuficiente (0) |
|----------|---------------|-----------|-------------|------------------|
| **Ports definidos** | Todos los ports con Protocols bien documentados | Ports correctos pero documentación mínima | Algunos ports, inconsistencias | No usa Protocols |
| **Adapters implementados** | 4+ adapters funcionando (Email, SMS, Push, Webhook) | 3 adapters funcionando | 2 adapters | Solo 1 o ninguno |
| **Inversión de dependencias** | Services solo dependen de ports | Mayoría usa ports | Mezcla ports y adapters concretos | Dependencias directas |
| **Testing** | Tests con fake adapters, >80% cobertura | Tests básicos con fakes | Algunos tests sin fakes | Sin tests |
| **API REST** | Endpoints completos, validación, errores | Endpoints funcionando | Endpoints básicos | API incompleta |

#### Estructura Esperada

```
3-proyecto/
└── starter/
    ├── src/
    │   ├── main.py
    │   ├── config.py
    │   ├── domain/
    │   │   ├── entities/
    │   │   │   └── notification.py
    │   │   └── ports/
    │   │       ├── __init__.py
    │   │       ├── notification_sender.py
    │   │       ├── notification_repository.py
    │   │       └── template_renderer.py
    │   ├── application/
    │   │   ├── services/
    │   │   │   └── notification_service.py
    │   │   └── dtos/
    │   │       └── notification_dtos.py
    │   ├── infrastructure/
    │   │   ├── adapters/
    │   │   │   ├── email_adapter.py
    │   │   │   ├── sms_adapter.py
    │   │   │   ├── push_adapter.py
    │   │   │   ├── webhook_adapter.py
    │   │   │   └── fake_adapter.py
    │   │   ├── persistence/
    │   │   │   └── sqlalchemy_notification_repository.py
    │   │   └── templates/
    │   │       └── jinja_template_renderer.py
    │   └── presentation/
    │       ├── routers/
    │       │   └── notifications.py
    │       └── dependencies.py
    └── tests/
        ├── unit/
        │   ├── test_notification_service.py
        │   └── fakes/
        │       └── fake_adapters.py
        └── integration/
            └── test_api.py
```

#### Funcionalidades Requeridas

| Funcionalidad | Puntos | Descripción |
|---------------|--------|-------------|
| Enviar notificación | 5 | POST /notifications |
| Múltiples canales | 5 | Email, SMS, Push, Webhook |
| Historial | 5 | GET /notifications |
| Templates | 5 | Renderizado de plantillas |
| Retry logic | 5 | Reintentos en fallos |
| Tests | 5 | Cobertura con fakes |

---

## 📈 Escala de Calificación

| Puntuación | Calificación | Descripción |
|------------|--------------|-------------|
| 90-100 | ⭐ Excelente | Dominio completo de Ports & Adapters |
| 80-89 | ✅ Muy Bueno | Buen entendimiento, detalles menores |
| 70-79 | 👍 Bueno | Cumple requisitos básicos |
| 60-69 | ⚠️ Regular | Necesita refuerzo |
| < 60 | ❌ Insuficiente | No cumple objetivos mínimos |

---

## 🎯 Criterios de Aprobación

Para aprobar esta semana necesitas:

- [ ] Mínimo **70%** en Conocimiento (21/30 pts)
- [ ] Mínimo **70%** en Desempeño (28/40 pts)
- [ ] Mínimo **70%** en Producto (21/30 pts)
- [ ] **Total mínimo**: 70 pts

---

## 📝 Entrega

### Formato de Entrega

```
week-09-nombre-apellido/
├── practicas/
│   ├── 01-definir-ports/
│   ├── 02-crear-adapters/
│   ├── 03-inyeccion-dependencias/
│   └── 04-testing-con-mocks/
└── proyecto/
    ├── src/
    ├── tests/
    ├── Dockerfile
    ├── docker-compose.yml
    └── README.md
```

### Fecha Límite

- **Prácticas**: Fin del día 3 de la semana
- **Proyecto**: Fin del día 4 de la semana

---

## 💡 Consejos para Éxito

1. **Piensa en contratos primero**: Define qué necesita tu dominio antes de cómo lo implementarás
2. **Protocol es tu amigo**: Úsalo para definir interfaces claras
3. **No mezcles capas**: El dominio NO debe importar infraestructura
4. **Fake > Mock**: Prefiere fake adapters sobre mocks complejos
5. **Testing revela diseño**: Si es difícil testear, el diseño puede mejorar

---

## 🔗 Referencias

- [typing.Protocol Documentation](https://docs.python.org/3/library/typing.html#typing.Protocol)
- [Dependency Inversion Principle](https://en.wikipedia.org/wiki/Dependency_inversion_principle)
- [Ports & Adapters Pattern](https://alistair.cockburn.us/hexagonal-architecture/)

---

_Rúbrica Semana 09 | Versión 1.0 | Enero 2026_
