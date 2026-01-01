"""
Dependencies - Inyección de dependencias para FastAPI.

Aquí se configuran y proveen las dependencias que se inyectarán
en los endpoints. Este es el punto donde conectamos la infraestructura
con la aplicación.
"""
from functools import lru_cache

from src.config import settings
from src.domain.entities.notification import NotificationChannel
from src.domain.ports.notification_sender import NotificationSender
from src.domain.ports.notification_repository import NotificationRepository
from src.application.services.notification_service import NotificationService

# Importar adaptadores
from src.infrastructure.adapters.console_adapter import ConsoleNotificationSender
from src.infrastructure.adapters.email_adapter import EmailNotificationSender
from src.infrastructure.adapters.sms_adapter import SMSNotificationSender
from src.infrastructure.adapters.push_adapter import PushNotificationSender
from src.infrastructure.adapters.webhook_adapter import WebhookNotificationSender
from src.infrastructure.persistence.in_memory_repository import InMemoryNotificationRepository


# ============================================
# Instancias singleton de adaptadores
# ============================================

# Repository (único para toda la aplicación)
_repository: NotificationRepository | None = None


def get_repository() -> NotificationRepository:
    """
    Obtiene el repositorio (singleton).
    
    TODO: Implementar:
    1. Usar variable global _repository
    2. Si es None, crear InMemoryNotificationRepository
    3. Retornar la instancia
    """
    global _repository
    # TODO: Implementar
    pass


# ============================================
# Factory de Senders
# ============================================

def create_senders() -> dict[NotificationChannel, NotificationSender]:
    """
    Crea el diccionario de senders por canal.
    
    Según la configuración, puede crear diferentes tipos de senders.
    
    TODO: Implementar:
    1. Crear un diccionario vacío
    2. Crear instancia de cada sender (Email, SMS, Push, Webhook)
    3. Mapear cada sender a su canal correspondiente
    4. Retornar el diccionario
    
    Returns:
        Dict[NotificationChannel, NotificationSender]
    """
    # TODO: Implementar
    pass


# ============================================
# Dependencia principal: NotificationService
# ============================================

_service: NotificationService | None = None


def get_notification_service() -> NotificationService:
    """
    Obtiene el servicio de notificaciones (singleton).
    
    Esta es la dependencia principal que se inyecta en los endpoints.
    
    TODO: Implementar:
    1. Usar variable global _service
    2. Si es None, crear NotificationService con:
       - senders = create_senders()
       - repository = get_repository()
    3. Retornar la instancia
    
    Uso en endpoints:
        @router.post("/")
        async def send(
            service: NotificationService = Depends(get_notification_service)
        ):
            ...
    """
    global _service
    # TODO: Implementar
    pass


# ============================================
# Utilidades para testing
# ============================================

def reset_dependencies() -> None:
    """
    Resetea las dependencias (para testing).
    
    Permite crear nuevas instancias en cada test.
    """
    global _repository, _service
    _repository = None
    _service = None


def override_repository(repo: NotificationRepository) -> None:
    """
    Sobrescribe el repositorio (para testing).
    
    Args:
        repo: Repositorio a usar (puede ser un fake)
    """
    global _repository
    _repository = repo


def override_service(service: NotificationService) -> None:
    """
    Sobrescribe el servicio (para testing).
    
    Args:
        service: Servicio a usar (puede tener fakes inyectados)
    """
    global _service
    _service = service
