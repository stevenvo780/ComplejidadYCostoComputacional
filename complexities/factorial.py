def compute(n):
    """Complejidad O(n!) - Tiempo Factorial"""
    if n <= 1:
        return 1
    total = 0
    for _ in range(n):
        total += compute(n-1)
    return total
