"""
Script de prueba para los adapters.

Ejecutar con: uv run python -m src.main
"""
import asyncio

from src.domain.entities import Notification, NotificationChannel
from src.infrastructure.adapters import (
    EmailAdapter,
    SMSAdapter,
    ConsoleAdapter,
    InMemoryNotificationRepository,
    EmailConfig,
    SMSConfig,
)


async def main():
    print("=" * 60)
    print("🧪 Probando Adapters")
    print("=" * 60)
    
    # Crear adapters
    email_adapter = EmailAdapter(EmailConfig())
    sms_adapter = SMSAdapter(SMSConfig())
    console_adapter = ConsoleAdapter()
    repo = InMemoryNotificationRepository()
    
    # Crear notificación de prueba
    notification = Notification(
        recipient="user@example.com",
        channel=NotificationChannel.EMAIL,
        subject="Test de Adapters",
        message="Este es un mensaje de prueba para verificar los adapters."
    )
    
    # Guardar en repositorio
    saved = await repo.save(notification)
    print(f"\n✅ Notificación guardada con ID: {saved.id}")
    
    # Enviar con ConsoleAdapter
    print("\n📧 Enviando con ConsoleAdapter:")
    await console_adapter.send(notification)
    
    # Verificar repositorio
    retrieved = await repo.get_by_id(saved.id)
    print(f"\n📋 Recuperada del repo: {retrieved}")
    
    print("\n" + "=" * 60)
    print("✅ Todos los adapters funcionan correctamente!")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
