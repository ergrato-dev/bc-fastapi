# ============================================
# USER REPOSITORY
# ============================================

# Descomenta las siguientes líneas:

# from sqlalchemy.orm import Session
# from models.user import User


# class UserRepository:
#     def __init__(self, db: Session):
#         self.db = db
#     
#     def get_by_id(self, user_id: int) -> User | None:
#         return self.db.get(User, user_id)
#     
#     def add(self, user: User) -> User:
#         self.db.add(user)
#         self.db.commit()
#         self.db.refresh(user)
#         return user
