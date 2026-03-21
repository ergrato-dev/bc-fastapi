"""
Adapter: EmailNotificationSender

Implementación de NotificationSender para envío de emails.
"""
from src.domain.entities.notification import Notification, NotificationChannel
from src.domain.ports.notification_sender import NotificationSender
from src.config import settings


class EmailNotificationSender:
    """
    Adapter que envía notificaciones por email.
    
    Implementa el Protocol NotificationSender.
    En producción usaría SMTP o un servicio como SendGrid/SES.
    
    TODO: Implementa los métodos para cumplir con el Protocol.
    """
    
    def __init__(
        self,
        host: str | None = None,
        port: int | None = None,
        username: str | None = None,
        password: str | None = None,
        from_email: str | None = None,
    ):
        """
        Inicializa el adapter con configuración SMTP.
        
        Args:
            host: Servidor SMTP
            port: Puerto SMTP
            username: Usuario SMTP
            password: Contraseña SMTP
            from_email: Email remitente
        """
        self._host = host or settings.smtp_host
        self._port = port or settings.smtp_port
        self._username = username or settings.smtp_username
        self._password = password or settings.smtp_password
        self._from_email = from_email or settings.smtp_from
    
    @property
    def channel(self) -> NotificationChannel:
        """Este adapter maneja el canal EMAIL."""
        return NotificationChannel.EMAIL
    
    async def send(self, notification: Notification) -> bool:
        """
        Envía un email.
        
        Args:
            notification: Notificación con datos del email
            
        Returns:
            True si se envió, False si falló
            
        TODO: Implementar:
        1. Validar que recipient sea un email válido
        2. En desarrollo: simular envío (print + return True)
        3. En producción: usar smtplib o servicio externo
        4. Manejar excepciones y retornar False si falla
        
        Nota: Para este proyecto, simula el envío con un print.
        """
        # TODO: Implementar
        pass
    
    async def send_batch(self, notifications: list[Notification]) -> dict[str, bool]:
        """
        Envía múltiples emails.
        
        Args:
            notifications: Lista de notificaciones
            
        Returns:
            Dict {notification_id: success}
            
        TODO: Implementar iterando sobre notifications y usando send().
        """
        # TODO: Implementar
        pass
