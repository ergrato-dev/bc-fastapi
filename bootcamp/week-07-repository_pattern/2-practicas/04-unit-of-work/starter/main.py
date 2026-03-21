# ============================================
# Script de prueba Unit of Work
# ============================================
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Account
# from unit_of_work import UnitOfWork
# from services import TransferService, NotFoundError, InsufficientFundsError

# Setup
DATABASE_URL = "sqlite:///./bank.db"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

# Crear tablas
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


def setup_accounts(db):
    """Crea cuentas de prueba"""
    alice = Account(owner="Alice", balance=1000.0)
    bob = Account(owner="Bob", balance=500.0)
    db.add_all([alice, bob])
    db.commit()
    return alice.id, bob.id


def main():
    print("\n" + "="*50)
    print("PRUEBA DE UNIT OF WORK")
    print("="*50)
    
    # Setup
    db = SessionLocal()
    alice_id, bob_id = setup_accounts(db)
    print(f"\nCuentas creadas: Alice (ID={alice_id}), Bob (ID={bob_id})")
    db.close()
    
    # ============================================
    # Descomenta para probar:
    # ============================================
    
    # # --- Prueba 1: Transferencia exitosa ---
    # print("\n--- Prueba 1: Transferencia exitosa ---")
    # db = SessionLocal()
    # with UnitOfWork(db) as uow:
    #     service = TransferService(uow)
    #     
    #     print(f"Balance Alice antes: {service.get_account_balance(alice_id)}")
    #     print(f"Balance Bob antes: {service.get_account_balance(bob_id)}")
    #     
    #     transfer = service.transfer(alice_id, bob_id, 200.0)
    #     uow.commit()
    #     
    #     print(f"\nTransferencia realizada: ${transfer.amount}")
    #     print(f"Balance Alice después: {service.get_account_balance(alice_id)}")
    #     print(f"Balance Bob después: {service.get_account_balance(bob_id)}")
    # db.close()
    # 
    # # --- Prueba 2: Fondos insuficientes (rollback) ---
    # print("\n--- Prueba 2: Fondos insuficientes ---")
    # db = SessionLocal()
    # with UnitOfWork(db) as uow:
    #     service = TransferService(uow)
    #     
    #     try:
    #         # Intentar transferir más de lo que tiene Alice
    #         service.transfer(alice_id, bob_id, 10000.0)
    #         uow.commit()
    #     except InsufficientFundsError as e:
    #         print(f"Error esperado: {e}")
    #         uow.rollback()
    #     
    #     # Verificar que los balances no cambiaron
    #     print(f"Balance Alice (sin cambios): {service.get_account_balance(alice_id)}")
    #     print(f"Balance Bob (sin cambios): {service.get_account_balance(bob_id)}")
    # db.close()
    # 
    # # --- Prueba 3: Cuenta no existe (rollback) ---
    # print("\n--- Prueba 3: Cuenta no existe ---")
    # db = SessionLocal()
    # with UnitOfWork(db) as uow:
    #     service = TransferService(uow)
    #     
    #     try:
    #         service.transfer(alice_id, 999, 100.0)
    #         uow.commit()
    #     except NotFoundError as e:
    #         print(f"Error esperado: {e}")
    # db.close()
    # 
    # # --- Prueba 4: Ver historial de transferencias ---
    # print("\n--- Prueba 4: Historial de transferencias ---")
    # db = SessionLocal()
    # with UnitOfWork(db) as uow:
    #     service = TransferService(uow)
    #     
    #     transfers = service.get_account_transfers(alice_id)
    #     print(f"Transferencias de Alice: {len(transfers)}")
    #     for t in transfers:
    #         print(f"  - ${t.amount} de cuenta {t.from_account_id} a cuenta {t.to_account_id}")
    # db.close()
    
    print("\n✅ Descomentar código en main.py, unit_of_work.py y services.py")
    print("="*50)


if __name__ == "__main__":
    main()
