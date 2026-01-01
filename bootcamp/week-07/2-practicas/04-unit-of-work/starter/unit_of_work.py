# ============================================
# PASO 2: Implementar Unit of Work
# ============================================
"""
Unit of Work coordina múltiples repositorios
en una sola transacción.
"""

from sqlalchemy.orm import Session

from repositories import AccountRepository, TransferRepository


# ============================================
# Descomenta UnitOfWork:
# ============================================

# class UnitOfWork:
#     """
#     Coordina transacciones entre repositorios.
#     
#     Uso:
#         with UnitOfWork(session) as uow:
#             account = uow.accounts.get_by_id(1)
#             account.balance += 100
#             uow.commit()
#     """
#     
#     def __init__(self, session: Session):
#         self._session = session
#     
#     def __enter__(self) -> "UnitOfWork":
#         """Crea repositorios con la misma sesión"""
#         self.accounts = AccountRepository(self._session)
#         self.transfers = TransferRepository(self._session)
#         return self
#     
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         """Rollback automático si hay excepción"""
#         if exc_type is not None:
#             self.rollback()
#     
#     def commit(self) -> None:
#         """Confirma todos los cambios"""
#         self._session.commit()
#     
#     def rollback(self) -> None:
#         """Revierte todos los cambios"""
#         self._session.rollback()
