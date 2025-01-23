def compute(n):
    """Complejidad O(log n) - Tiempo Logarítmico"""
    result = 0
    i = n
    while i > 0:
        result += 1
        i = i // 2
    return result
