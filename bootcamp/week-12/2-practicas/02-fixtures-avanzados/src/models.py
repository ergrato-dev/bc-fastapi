"""
Modelos de datos para practicar fixtures.

Estos modelos simulan entidades de una aplicación real.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import ClassVar


@dataclass
class User:
    """Modelo de usuario."""
    
    id: int
    email: str
    name: str
    is_active: bool = True
    created_at: datetime = field(default_factory=datetime.now)
    
    _id_counter: ClassVar[int] = 0
    
    @classmethod
    def create(cls, email: str, name: str) -> "User":
        """Factory method para crear usuarios."""
        cls._id_counter += 1
        return cls(id=cls._id_counter, email=email, name=name)
    
    @classmethod
    def reset_counter(cls) -> None:
        """Reset del contador de IDs."""
        cls._id_counter = 0


@dataclass
class Product:
    """Modelo de producto."""
    
    id: int
    name: str
    price: float
    stock: int = 0
    
    _id_counter: ClassVar[int] = 0
    
    @classmethod
    def create(cls, name: str, price: float, stock: int = 0) -> "Product":
        """Factory method para crear productos."""
        cls._id_counter += 1
        return cls(id=cls._id_counter, name=name, price=price, stock=stock)
    
    @classmethod
    def reset_counter(cls) -> None:
        """Reset del contador de IDs."""
        cls._id_counter = 0


@dataclass
class Order:
    """Modelo de orden."""
    
    id: int
    user_id: int
    items: list[dict] = field(default_factory=list)
    total: float = 0.0
    status: str = "pending"
    
    _id_counter: ClassVar[int] = 0
    
    @classmethod
    def create(cls, user_id: int) -> "Order":
        """Factory method para crear órdenes."""
        cls._id_counter += 1
        return cls(id=cls._id_counter, user_id=user_id)
    
    @classmethod
    def reset_counter(cls) -> None:
        """Reset del contador de IDs."""
        cls._id_counter = 0
    
    def add_item(self, product: Product, quantity: int) -> None:
        """Añadir producto a la orden."""
        self.items.append({
            "product_id": product.id,
            "name": product.name,
            "price": product.price,
            "quantity": quantity,
        })
        self.total += product.price * quantity


class Database:
    """Simulador de base de datos en memoria."""
    
    def __init__(self):
        self.users: dict[int, User] = {}
        self.products: dict[int, Product] = {}
        self.orders: dict[int, Order] = {}
        self._connected = False
    
    def connect(self) -> None:
        """Conectar a la base de datos."""
        print("  📦 Database: Connecting...")
        self._connected = True
    
    def disconnect(self) -> None:
        """Desconectar de la base de datos."""
        print("  📦 Database: Disconnecting...")
        self._connected = False
    
    def is_connected(self) -> bool:
        """Verificar si está conectada."""
        return self._connected
    
    def add_user(self, user: User) -> User:
        """Añadir usuario."""
        self.users[user.id] = user
        return user
    
    def get_user(self, user_id: int) -> User | None:
        """Obtener usuario por ID."""
        return self.users.get(user_id)
    
    def add_product(self, product: Product) -> Product:
        """Añadir producto."""
        self.products[product.id] = product
        return product
    
    def get_product(self, product_id: int) -> Product | None:
        """Obtener producto por ID."""
        return self.products.get(product_id)
    
    def clear(self) -> None:
        """Limpiar todos los datos."""
        self.users.clear()
        self.products.clear()
        self.orders.clear()
