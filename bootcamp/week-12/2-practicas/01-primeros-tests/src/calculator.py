"""
Calculator module with basic arithmetic operations.

Este módulo contiene funciones matemáticas básicas que usaremos
para aprender a escribir tests con pytest.
"""


def add(a: int | float, b: int | float) -> int | float:
    """
    Suma dos números.
    
    Args:
        a: Primer número
        b: Segundo número
        
    Returns:
        La suma de a y b
    """
    return a + b


def subtract(a: int | float, b: int | float) -> int | float:
    """
    Resta dos números.
    
    Args:
        a: Minuendo
        b: Sustraendo
        
    Returns:
        La diferencia a - b
    """
    return a - b


def multiply(a: int | float, b: int | float) -> int | float:
    """
    Multiplica dos números.
    
    Args:
        a: Primer factor
        b: Segundo factor
        
    Returns:
        El producto de a y b
    """
    return a * b


def divide(a: int | float, b: int | float) -> float:
    """
    Divide dos números.
    
    Args:
        a: Dividendo
        b: Divisor
        
    Returns:
        El cociente a / b
        
    Raises:
        ValueError: Si b es cero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base: int | float, exponent: int | float) -> int | float:
    """
    Calcula la potencia.
    
    Args:
        base: Base de la potencia
        exponent: Exponente
        
    Returns:
        base elevado a exponent
    """
    return base ** exponent


def is_even(n: int) -> bool:
    """
    Verifica si un número es par.
    
    Args:
        n: Número entero a verificar
        
    Returns:
        True si es par, False si es impar
    """
    return n % 2 == 0


def factorial(n: int) -> int:
    """
    Calcula el factorial de un número.
    
    Args:
        n: Número entero no negativo
        
    Returns:
        n! (factorial de n)
        
    Raises:
        ValueError: Si n es negativo
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    """
    Calcula el n-ésimo número de Fibonacci.
    
    Args:
        n: Posición en la secuencia (0-indexed)
        
    Returns:
        El n-ésimo número de Fibonacci
        
    Raises:
        ValueError: Si n es negativo
    """
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative indices")
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def is_prime(n: int) -> bool:
    """
    Verifica si un número es primo.
    
    Args:
        n: Número entero a verificar
        
    Returns:
        True si es primo, False en caso contrario
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
