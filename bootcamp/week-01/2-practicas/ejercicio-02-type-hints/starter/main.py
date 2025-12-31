# ============================================
# TYPE HINTS EN PRÁCTICA
# ============================================
# Este ejercicio te ayudará a practicar el uso
# de type hints en Python 3.13+

print("=" * 50)
print("Ejercicio 02: Type Hints en Práctica")
print("=" * 50)


# ============================================
# PASO 1: Tipos Básicos
# ============================================
print("\n--- Paso 1: Tipos Básicos ---")

# Los tipos básicos son: str, int, float, bool
# Descomenta las siguientes funciones:

# def greet(name: str) -> str:
#     """Retorna un saludo personalizado."""
#     return f"¡Hola, {name}!"


# def calculate_area(width: float, height: float) -> float:
#     """Calcula el área de un rectángulo."""
#     return width * height


# def is_adult(age: int) -> bool:
#     """Verifica si una persona es mayor de edad."""
#     return age >= 18


# Descomenta para probar:
# print(greet("Carlos"))                    # ¡Hola, Carlos!
# print(calculate_area(5.0, 3.0))           # 15.0
# print(is_adult(25))                       # True
# print(is_adult(16))                       # False


# ============================================
# PASO 2: Tipos Compuestos
# ============================================
print("\n--- Paso 2: Tipos Compuestos ---")

# En Python 3.9+ usamos list[], dict[], set[] directamente
# Descomenta las siguientes funciones:

# def sum_numbers(numbers: list[int]) -> int:
#     """Suma todos los números de una lista."""
#     return sum(numbers)


# def get_user_emails(users: list[dict[str, str]]) -> list[str]:
#     """Extrae los emails de una lista de usuarios."""
#     return [user["email"] for user in users]


# def count_words(text: str) -> dict[str, int]:
#     """Cuenta las ocurrencias de cada palabra."""
#     words = text.lower().split()
#     result: dict[str, int] = {}
#     for word in words:
#         result[word] = result.get(word, 0) + 1
#     return result


# Descomenta para probar:
# print(sum_numbers([1, 2, 3, 4, 5]))        # 15
# 
# users = [
#     {"name": "Alice", "email": "alice@example.com"},
#     {"name": "Bob", "email": "bob@example.com"},
# ]
# print(get_user_emails(users))             # ['alice@example.com', 'bob@example.com']
# 
# print(count_words("hola mundo hola"))     # {'hola': 2, 'mundo': 1}


# ============================================
# PASO 3: Tipos Opcionales (Union con None)
# ============================================
print("\n--- Paso 3: Tipos Opcionales ---")

# Cuando un valor puede ser None, usamos | None (Python 3.10+)
# Descomenta las siguientes funciones:

# def find_item(items: list[str], target: str) -> str | None:
#     """Busca un item en la lista, retorna None si no existe."""
#     if target in items:
#         return target
#     return None


# def get_first_element(items: list[int]) -> int | None:
#     """Retorna el primer elemento o None si la lista está vacía."""
#     if items:
#         return items[0]
#     return None


# def parse_int(value: str) -> int | None:
#     """Intenta convertir un string a int, retorna None si falla."""
#     try:
#         return int(value)
#     except ValueError:
#         return None


# Descomenta para probar:
# fruits = ["apple", "banana", "cherry"]
# print(find_item(fruits, "banana"))        # banana
# print(find_item(fruits, "mango"))         # None
# 
# print(get_first_element([10, 20, 30]))    # 10
# print(get_first_element([]))              # None
# 
# print(parse_int("42"))                    # 42
# print(parse_int("abc"))                   # None


# ============================================
# PASO 4: Parámetros con Valores por Defecto
# ============================================
print("\n--- Paso 4: Parámetros por Defecto ---")

# Los parámetros opcionales tienen un valor por defecto
# Descomenta las siguientes funciones:

# def create_user(
#     name: str,
#     email: str,
#     age: int = 0,
#     is_active: bool = True,
# ) -> dict[str, str | int | bool]:
#     """Crea un diccionario de usuario."""
#     return {
#         "name": name,
#         "email": email,
#         "age": age,
#         "is_active": is_active,
#     }


# def paginate(
#     items: list[str],
#     page: int = 1,
#     per_page: int = 10,
# ) -> list[str]:
#     """Retorna una página de items."""
#     start = (page - 1) * per_page
#     end = start + per_page
#     return items[start:end]


# Descomenta para probar:
# print(create_user("Alice", "alice@example.com"))
# # {'name': 'Alice', 'email': 'alice@example.com', 'age': 0, 'is_active': True}
# 
# print(create_user("Bob", "bob@example.com", age=25, is_active=False))
# # {'name': 'Bob', 'email': 'bob@example.com', 'age': 25, 'is_active': False}
# 
# all_items = [f"item-{i}" for i in range(1, 26)]
# print(paginate(all_items, page=1))        # ['item-1', ..., 'item-10']
# print(paginate(all_items, page=2, per_page=5))  # ['item-6', ..., 'item-10']


# ============================================
# PASO 5: Type Aliases (Alias de Tipos)
# ============================================
print("\n--- Paso 5: Type Aliases ---")

# Los type aliases hacen el código más legible
# Descomenta las siguientes definiciones:

# # Definir alias para tipos complejos
# UserId = int
# Email = str
# UserData = dict[str, str | int]
# UserList = list[UserData]


# def get_user_by_id(user_id: UserId) -> UserData | None:
#     """Busca un usuario por ID."""
#     fake_db: UserList = [
#         {"id": 1, "name": "Alice", "email": "alice@example.com"},
#         {"id": 2, "name": "Bob", "email": "bob@example.com"},
#     ]
#     for user in fake_db:
#         if user["id"] == user_id:
#             return user
#     return None


# def get_user_email(user_id: UserId) -> Email | None:
#     """Obtiene el email de un usuario."""
#     user = get_user_by_id(user_id)
#     if user:
#         return str(user["email"])
#     return None


# Descomenta para probar:
# print(get_user_by_id(1))
# # {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'}
# 
# print(get_user_email(2))                  # bob@example.com
# print(get_user_email(99))                 # None


# ============================================
# VERIFICACIÓN FINAL
# ============================================
print("\n" + "=" * 50)
print("✅ Ejercicio completado!")
print("=" * 50)
print("""
Conceptos practicados:
- Tipos básicos: str, int, float, bool
- Tipos compuestos: list[], dict[], set[]
- Tipos opcionales: | None
- Parámetros por defecto
- Type aliases

Siguiente: Ejercicio 03 - Programación Asíncrona
""")
