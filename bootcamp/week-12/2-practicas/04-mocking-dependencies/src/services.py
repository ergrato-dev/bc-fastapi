"""
Services with external dependencies.

Estos servicios dependen de componentes externos que
necesitamos mockear en los tests.
"""

from datetime import datetime
from typing import Protocol


class EmailSenderProtocol(Protocol):
    """Protocol for email sender."""
    
    def send(self, to: str, subject: str, body: str) -> bool:
        """Send an email."""
        ...


class UserService:
    """Service for user operations."""
    
    def __init__(self, email_sender: EmailSenderProtocol):
        self.email_sender = email_sender
    
    def register_user(self, email: str, name: str) -> dict:
        """
        Register a new user and send welcome email.
        
        Args:
            email: User's email
            name: User's name
            
        Returns:
            User data dict
        """
        # Create user
        user = {
            "id": 1,
            "email": email,
            "name": name,
            "created_at": datetime.now().isoformat(),
        }
        
        # Send welcome email
        self.email_sender.send(
            to=email,
            subject="Welcome to our platform!",
            body=f"Hello {name}, welcome aboard!"
        )
        
        return user
    
    def reset_password(self, email: str) -> bool:
        """
        Send password reset email.
        
        Args:
            email: User's email
            
        Returns:
            True if email was sent
        """
        reset_link = f"https://example.com/reset?token=abc123"
        
        return self.email_sender.send(
            to=email,
            subject="Password Reset Request",
            body=f"Click here to reset: {reset_link}"
        )


class OrderService:
    """Service for order operations."""
    
    def __init__(self, payment_gateway, inventory_service):
        self.payment_gateway = payment_gateway
        self.inventory_service = inventory_service
    
    def create_order(self, user_id: int, items: list[dict]) -> dict:
        """
        Create a new order.
        
        Args:
            user_id: ID of the user
            items: List of items [{product_id, quantity}]
            
        Returns:
            Order data dict
        """
        # Check inventory
        for item in items:
            available = self.inventory_service.check_stock(
                item["product_id"],
                item["quantity"]
            )
            if not available:
                raise ValueError(f"Insufficient stock for product {item['product_id']}")
        
        # Calculate total
        total = sum(
            self.inventory_service.get_price(item["product_id"]) * item["quantity"]
            for item in items
        )
        
        # Process payment
        payment_result = self.payment_gateway.charge(user_id, total)
        if not payment_result["success"]:
            raise ValueError("Payment failed")
        
        # Reserve inventory
        for item in items:
            self.inventory_service.reserve(item["product_id"], item["quantity"])
        
        return {
            "id": 1,
            "user_id": user_id,
            "items": items,
            "total": total,
            "payment_id": payment_result["payment_id"],
            "status": "confirmed",
        }


def get_greeting() -> str:
    """
    Get a greeting based on current time.
    
    Returns:
        Greeting message
    """
    hour = datetime.now().hour
    
    if hour < 12:
        return "Good morning!"
    elif hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"


def calculate_age(birth_date: datetime) -> int:
    """
    Calculate age from birth date.
    
    Args:
        birth_date: Date of birth
        
    Returns:
        Age in years
    """
    today = datetime.now()
    age = today.year - birth_date.year
    
    # Adjust if birthday hasn't occurred this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    
    return age
