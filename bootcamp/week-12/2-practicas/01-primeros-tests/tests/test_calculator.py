"""
Tests para el módulo calculator.

Instrucciones:
1. Lee cada sección y entiende qué se está testeando
2. Descomenta el código de cada test
3. Ejecuta `uv run pytest -v` para verificar
4. Completa los tests marcados con TODO
"""

import pytest
from src.calculator import (
    add,
    subtract,
    multiply,
    divide,
    power,
    is_even,
    factorial,
    fibonacci,
    is_prime,
)


# ============================================
# PASO 1: Tests básicos de suma
# ============================================
print("--- Paso 1: Tests de suma ---")

# Test simple: verificar que 1 + 1 = 2
# Descomenta las siguientes líneas:

# def test_add_one_plus_one():
#     """Test básico de suma."""
#     result = add(1, 1)
#     assert result == 2


# Test con números positivos
# Descomenta las siguientes líneas:

# def test_add_two_positive_numbers():
#     """Suma de dos números positivos."""
#     result = add(5, 3)
#     assert result == 8


# Test con números negativos
# Descomenta las siguientes líneas:

# def test_add_negative_numbers():
#     """Suma de números negativos."""
#     assert add(-1, -1) == -2
#     assert add(-5, 3) == -2
#     assert add(5, -3) == 2


# Test con decimales (usando pytest.approx para floats)
# Descomenta las siguientes líneas:

# def test_add_floats():
#     """Suma de decimales con tolerancia."""
#     result = add(0.1, 0.2)
#     assert result == pytest.approx(0.3)


# ============================================
# PASO 2: Tests de resta y multiplicación
# ============================================
print("--- Paso 2: Tests de resta y multiplicación ---")

# Descomenta las siguientes líneas:

# def test_subtract_basic():
#     """Resta básica."""
#     assert subtract(10, 4) == 6
#     assert subtract(4, 10) == -6


# def test_multiply_basic():
#     """Multiplicación básica."""
#     assert multiply(3, 4) == 12
#     assert multiply(-2, 3) == -6
#     assert multiply(-2, -3) == 6


# def test_multiply_by_zero():
#     """Multiplicar por cero da cero."""
#     assert multiply(100, 0) == 0
#     assert multiply(0, 100) == 0


# ============================================
# PASO 3: Tests de división y excepciones
# ============================================
print("--- Paso 3: Tests de división ---")

# Test de división normal
# Descomenta las siguientes líneas:

# def test_divide_basic():
#     """División básica."""
#     assert divide(10, 2) == 5.0
#     assert divide(7, 2) == 3.5


# Test de excepción: división por cero
# Usamos pytest.raises para verificar que se lanza la excepción
# Descomenta las siguientes líneas:

# def test_divide_by_zero_raises_error():
#     """División por cero debe lanzar ValueError."""
#     with pytest.raises(ValueError):
#         divide(10, 0)


# Test verificando el mensaje de la excepción
# Descomenta las siguientes líneas:

# def test_divide_by_zero_error_message():
#     """Verificar mensaje de error en división por cero."""
#     with pytest.raises(ValueError) as exc_info:
#         divide(10, 0)
    
#     assert "zero" in str(exc_info.value).lower()


# ============================================
# PASO 4: Tests con parametrize
# ============================================
print("--- Paso 4: Tests parametrizados ---")

# Parametrize permite ejecutar el mismo test con diferentes datos
# Descomenta las siguientes líneas:

# @pytest.mark.parametrize("a, b, expected", [
#     (2, 3, 5),
#     (0, 0, 0),
#     (-1, 1, 0),
#     (100, 200, 300),
#     (1.5, 2.5, 4.0),
# ])
# def test_add_parametrized(a, b, expected):
#     """Test de suma con múltiples casos."""
#     assert add(a, b) == expected


# Parametrize para potencias
# Descomenta las siguientes líneas:

# @pytest.mark.parametrize("base, exp, expected", [
#     (2, 3, 8),
#     (3, 2, 9),
#     (10, 0, 1),
#     (5, 1, 5),
#     (2, 10, 1024),
# ])
# def test_power_parametrized(base, exp, expected):
#     """Test de potencias con múltiples casos."""
#     assert power(base, exp) == expected


# ============================================
# PASO 5: Tests de funciones booleanas
# ============================================
print("--- Paso 5: Tests de is_even ---")

# Descomenta las siguientes líneas:

# def test_is_even_with_even_numbers():
#     """Números pares retornan True."""
#     assert is_even(2) is True
#     assert is_even(0) is True
#     assert is_even(100) is True
#     assert is_even(-4) is True


# def test_is_even_with_odd_numbers():
#     """Números impares retornan False."""
#     assert is_even(1) is False
#     assert is_even(3) is False
#     assert is_even(-7) is False


# ============================================
# PASO 6: Tests de factorial
# ============================================
print("--- Paso 6: Tests de factorial ---")

# Descomenta las siguientes líneas:

# @pytest.mark.parametrize("n, expected", [
#     (0, 1),
#     (1, 1),
#     (5, 120),
#     (10, 3628800),
# ])
# def test_factorial_valid_inputs(n, expected):
#     """Factorial de números válidos."""
#     assert factorial(n) == expected


# def test_factorial_negative_raises_error():
#     """Factorial de negativo debe fallar."""
#     with pytest.raises(ValueError, match="negative"):
#         factorial(-1)


# ============================================
# PASO 7: Tests de Fibonacci
# ============================================
print("--- Paso 7: Tests de Fibonacci ---")

# Descomenta las siguientes líneas:

# @pytest.mark.parametrize("n, expected", [
#     (0, 0),
#     (1, 1),
#     (2, 1),
#     (3, 2),
#     (4, 3),
#     (5, 5),
#     (10, 55),
# ])
# def test_fibonacci_sequence(n, expected):
#     """Verificar secuencia de Fibonacci."""
#     assert fibonacci(n) == expected


# def test_fibonacci_negative_raises_error():
#     """Fibonacci de índice negativo debe fallar."""
#     with pytest.raises(ValueError):
#         fibonacci(-1)


# ============================================
# PASO 8: Tests de is_prime
# ============================================
print("--- Paso 8: Tests de números primos ---")

# Descomenta las siguientes líneas:

# @pytest.mark.parametrize("n", [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
# def test_prime_numbers(n):
#     """Verificar números primos conocidos."""
#     assert is_prime(n) is True


# @pytest.mark.parametrize("n", [0, 1, 4, 6, 8, 9, 10, 12, 15, 100])
# def test_non_prime_numbers(n):
#     """Verificar números no primos."""
#     assert is_prime(n) is False


# ============================================
# PASO 9: Agrupando tests con clases
# ============================================
print("--- Paso 9: Tests agrupados en clase ---")

# Las clases permiten agrupar tests relacionados
# Descomenta las siguientes líneas:

# class TestArithmeticOperations:
#     """Grupo de tests para operaciones aritméticas."""
    
#     def test_addition(self):
#         assert add(2, 2) == 4
    
#     def test_subtraction(self):
#         assert subtract(5, 3) == 2
    
#     def test_multiplication(self):
#         assert multiply(3, 3) == 9
    
#     def test_division(self):
#         assert divide(10, 2) == 5.0


# ============================================
# PASO 10: Markers personalizados
# ============================================
print("--- Paso 10: Markers ---")

# Los markers permiten categorizar y filtrar tests
# Ejecutar solo tests marcados: uv run pytest -m slow

# Descomenta las siguientes líneas:

# @pytest.mark.slow
# def test_large_factorial():
#     """Test marcado como lento."""
#     result = factorial(20)
#     assert result == 2432902008176640000


# @pytest.mark.skip(reason="Demonstrating skip")
# def test_skipped():
#     """Este test se salta."""
#     assert False  # Nunca se ejecuta


# @pytest.mark.xfail(reason="Known limitation")
# def test_expected_failure():
#     """Test que se espera que falle."""
#     # Este test fallará pero no romperá el suite
#     assert fibonacci(50) == 0  # Valor incorrecto a propósito
