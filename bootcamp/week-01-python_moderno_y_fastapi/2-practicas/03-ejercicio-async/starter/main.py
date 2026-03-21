# ============================================
# PROGRAMACIÓN ASÍNCRONA EN PRÁCTICA
# ============================================
# Este ejercicio te ayudará a entender async/await
# y cómo ejecutar tareas concurrentes.

import asyncio
import time

print("=" * 50)
print("Ejercicio 03: Programación Asíncrona")
print("=" * 50)


# ============================================
# PASO 1: Tu Primera Coroutine
# ============================================
print("\n--- Paso 1: Tu Primera Coroutine ---")

# Una coroutine se define con 'async def'
# Descomenta las siguientes funciones:

# async def say_hello() -> str:
#     """Una coroutine simple que retorna un saludo."""
#     return "¡Hola desde una coroutine!"


# async def say_hello_delayed(delay: float) -> str:
#     """Una coroutine que espera antes de retornar."""
#     await asyncio.sleep(delay)  # Espera NO bloqueante
#     return f"¡Hola después de {delay} segundos!"


# ============================================
# PASO 2: Ejecutar Coroutines con await
# ============================================
print("\n--- Paso 2: Ejecutar Coroutines ---")

# Para ejecutar una coroutine, necesitas 'await'
# Descomenta el siguiente bloque:

# async def test_coroutines():
#     # Llamar una coroutine sin await NO la ejecuta
#     # say_hello()  # Esto crea el objeto pero no lo ejecuta
#     
#     # Con await, la coroutine se ejecuta
#     result1 = await say_hello()
#     print(f"Resultado 1: {result1}")
#     
#     result2 = await say_hello_delayed(1.0)
#     print(f"Resultado 2: {result2}")


# ============================================
# PASO 3: Comparar Sync vs Async
# ============================================
print("\n--- Paso 3: Sync vs Async ---")

# Primero veamos cómo funciona el código síncrono
# Descomenta el siguiente bloque:

# def sync_task(name: str, duration: float) -> str:
#     """Tarea síncrona que bloquea."""
#     print(f"[SYNC] {name}: Iniciando...")
#     time.sleep(duration)  # BLOQUEA todo el programa
#     print(f"[SYNC] {name}: Completada")
#     return f"Resultado de {name}"


# def run_sync_tasks():
#     """Ejecuta tareas de forma síncrona (secuencial)."""
#     start = time.time()
#     
#     # Cada tarea espera a que termine la anterior
#     result1 = sync_task("Tarea A", 1)
#     result2 = sync_task("Tarea B", 1)
#     result3 = sync_task("Tarea C", 1)
#     
#     elapsed = time.time() - start
#     print(f"[SYNC] Tiempo total: {elapsed:.2f}s")
#     return [result1, result2, result3]


# Ahora la versión asíncrona
# Descomenta el siguiente bloque:

# async def async_task(name: str, duration: float) -> str:
#     """Tarea asíncrona que NO bloquea."""
#     print(f"[ASYNC] {name}: Iniciando...")
#     await asyncio.sleep(duration)  # NO bloquea, permite otras tareas
#     print(f"[ASYNC] {name}: Completada")
#     return f"Resultado de {name}"


# async def run_async_tasks():
#     """Ejecuta tareas de forma asíncrona (concurrente)."""
#     start = time.time()
#     
#     # Todas las tareas se ejecutan concurrentemente
#     results = await asyncio.gather(
#         async_task("Tarea A", 1),
#         async_task("Tarea B", 1),
#         async_task("Tarea C", 1),
#     )
#     
#     elapsed = time.time() - start
#     print(f"[ASYNC] Tiempo total: {elapsed:.2f}s")
#     return results


# ============================================
# PASO 4: asyncio.gather() en Detalle
# ============================================
print("\n--- Paso 4: asyncio.gather() ---")

# gather() ejecuta múltiples coroutines y espera a todas
# Descomenta el siguiente bloque:

# async def fetch_user(user_id: int) -> dict:
#     """Simula obtener un usuario de la base de datos."""
#     await asyncio.sleep(0.5)  # Simula latencia de DB
#     return {"id": user_id, "name": f"Usuario {user_id}"}


# async def fetch_posts(user_id: int) -> list[dict]:
#     """Simula obtener los posts de un usuario."""
#     await asyncio.sleep(0.5)  # Simula latencia de DB
#     return [
#         {"id": 1, "title": "Post 1", "user_id": user_id},
#         {"id": 2, "title": "Post 2", "user_id": user_id},
#     ]


# async def fetch_comments(post_id: int) -> list[dict]:
#     """Simula obtener comentarios de un post."""
#     await asyncio.sleep(0.5)  # Simula latencia de DB
#     return [
#         {"id": 1, "text": "Comentario 1", "post_id": post_id},
#         {"id": 2, "text": "Comentario 2", "post_id": post_id},
#     ]


# async def get_user_dashboard(user_id: int) -> dict:
#     """Obtiene toda la información del dashboard del usuario."""
#     start = time.time()
#     
#     # Ejecutar queries en paralelo
#     user, posts = await asyncio.gather(
#         fetch_user(user_id),
#         fetch_posts(user_id),
#     )
#     
#     # Los comentarios dependen de los posts
#     # Obtener comentarios de todos los posts en paralelo
#     all_comments = await asyncio.gather(
#         *[fetch_comments(post["id"]) for post in posts]
#     )
#     
#     elapsed = time.time() - start
#     print(f"Dashboard cargado en {elapsed:.2f}s")
#     
#     return {
#         "user": user,
#         "posts": posts,
#         "comments": all_comments,
#     }


# ============================================
# PASO 5: Manejo de Errores en Async
# ============================================
print("\n--- Paso 5: Manejo de Errores ---")

# Los errores en async se manejan igual que en sync
# Descomenta el siguiente bloque:

# async def risky_operation(should_fail: bool) -> str:
#     """Operación que puede fallar."""
#     await asyncio.sleep(0.1)
#     if should_fail:
#         raise ValueError("¡Algo salió mal!")
#     return "Operación exitosa"


# async def safe_operation():
#     """Demuestra manejo de errores en async."""
#     try:
#         result = await risky_operation(should_fail=True)
#         print(f"Resultado: {result}")
#     except ValueError as e:
#         print(f"Error capturado: {e}")
#     finally:
#         print("Limpieza completada")


# ============================================
# PASO 6: Timeout con asyncio
# ============================================
print("\n--- Paso 6: Timeout ---")

# asyncio.wait_for() permite establecer un timeout
# Descomenta el siguiente bloque:

# async def slow_operation() -> str:
#     """Operación que tarda mucho tiempo."""
#     await asyncio.sleep(10)  # Tarda 10 segundos
#     return "Completada"


# async def operation_with_timeout():
#     """Ejecuta una operación con límite de tiempo."""
#     try:
#         result = await asyncio.wait_for(
#             slow_operation(),
#             timeout=2.0  # Máximo 2 segundos
#         )
#         print(f"Resultado: {result}")
#     except asyncio.TimeoutError:
#         print("⏰ La operación tardó demasiado!")


# ============================================
# FUNCIÓN PRINCIPAL
# ============================================

# async def main():
#     """Ejecuta todos los ejemplos."""
#     
#     # Paso 2: Coroutines básicas
#     print("\n" + "=" * 40)
#     print("Ejecutando coroutines básicas...")
#     await test_coroutines()
#     
#     # Paso 3: Comparación sync vs async
#     print("\n" + "=" * 40)
#     print("Comparando SYNC (secuencial):")
#     run_sync_tasks()
#     
#     print("\n" + "=" * 40)
#     print("Comparando ASYNC (concurrente):")
#     await run_async_tasks()
#     
#     # Paso 4: Dashboard con gather
#     print("\n" + "=" * 40)
#     print("Cargando dashboard...")
#     dashboard = await get_user_dashboard(user_id=1)
#     print(f"Usuario: {dashboard['user']['name']}")
#     print(f"Posts: {len(dashboard['posts'])}")
#     
#     # Paso 5: Manejo de errores
#     print("\n" + "=" * 40)
#     print("Manejando errores...")
#     await safe_operation()
#     
#     # Paso 6: Timeout
#     print("\n" + "=" * 40)
#     print("Probando timeout...")
#     await operation_with_timeout()


# ============================================
# PUNTO DE ENTRADA
# ============================================

# Descomenta para ejecutar:
# if __name__ == "__main__":
#     asyncio.run(main())


# ============================================
# VERIFICACIÓN FINAL
# ============================================
print("\n" + "=" * 50)
print("Para ejecutar este ejercicio:")
print("1. Descomenta todas las secciones")
print("2. Descomenta 'asyncio.run(main())' al final")
print("3. Ejecuta: docker compose run --rm api python src/main.py")
print("=" * 50)
