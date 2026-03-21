# ============================================
# PASO 3: Service con Unit of Work
# ============================================
"""
El TransferService usa UnitOfWork para garantizar
que las transferencias son atómicas.
"""

from models import Transfer
# from unit_of_work import UnitOfWork


# ============================================
# Excepciones
# ============================================
class NotFoundError(Exception):
    pass


class InsufficientFundsError(Exception):
    pass


# ============================================
# Descomenta TransferService:
# ============================================

# class TransferService:
#     """
#     Service para transferencias bancarias.
#     Usa UnitOfWork para transacciones atómicas.
#     """
#     
#     def __init__(self, uow: UnitOfWork):
#         self.uow = uow
#     
#     def transfer(
#         self,
#         from_account_id: int,
#         to_account_id: int,
#         amount: float
#     ) -> Transfer:
#         """
#         Transfiere dinero entre cuentas.
#         
#         Esta operación DEBE ser atómica:
#         - Debitar cuenta origen
#         - Acreditar cuenta destino
#         - Registrar transferencia
#         
#         Si cualquier paso falla, TODO se revierte.
#         """
#         # Validar monto
#         if amount <= 0:
#             raise ValueError("Amount must be positive")
#         
#         # Obtener cuentas
#         from_account = self.uow.accounts.get_by_id(from_account_id)
#         if not from_account:
#             raise NotFoundError(f"Source account {from_account_id} not found")
#         
#         to_account = self.uow.accounts.get_by_id(to_account_id)
#         if not to_account:
#             raise NotFoundError(f"Destination account {to_account_id} not found")
#         
#         # Validar fondos
#         if from_account.balance < amount:
#             raise InsufficientFundsError(
#                 f"Insufficient funds. Balance: {from_account.balance}, Amount: {amount}"
#             )
#         
#         # Realizar transferencia (TODO es atómico gracias a UoW)
#         from_account.balance -= amount
#         to_account.balance += amount
#         
#         # Actualizar cuentas
#         self.uow.accounts.update(from_account)
#         self.uow.accounts.update(to_account)
#         
#         # Registrar transferencia
#         transfer = Transfer(
#             from_account_id=from_account_id,
#             to_account_id=to_account_id,
#             amount=amount
#         )
#         return self.uow.transfers.add(transfer)
#     
#     def get_account_balance(self, account_id: int) -> float:
#         """Obtiene balance de una cuenta"""
#         account = self.uow.accounts.get_by_id(account_id)
#         if not account:
#             raise NotFoundError(f"Account {account_id} not found")
#         return account.balance
#     
#     def get_account_transfers(self, account_id: int) -> list[Transfer]:
#         """Obtiene transferencias de una cuenta"""
#         account = self.uow.accounts.get_by_id(account_id)
#         if not account:
#             raise NotFoundError(f"Account {account_id} not found")
#         return self.uow.transfers.get_by_account(account_id)
