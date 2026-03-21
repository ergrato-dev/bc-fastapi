# ============================================
# Modelos para Transfer System
# ============================================
from datetime import datetime
from sqlalchemy import String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    pass


class Account(Base):
    """Cuenta bancaria"""
    __tablename__ = "accounts"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    owner: Mapped[str] = mapped_column(String(100))
    balance: Mapped[float] = mapped_column(Float, default=0.0)


class Transfer(Base):
    """Registro de transferencia"""
    __tablename__ = "transfers"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    from_account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"))
    to_account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"))
    amount: Mapped[float] = mapped_column(Float)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
