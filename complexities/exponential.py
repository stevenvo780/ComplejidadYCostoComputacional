def compute(n):
    """Complejidad O(2ⁿ) - Tiempo Exponencial"""
    if n <= 1:
        return n
    return compute(n-1) + compute(n-2)
