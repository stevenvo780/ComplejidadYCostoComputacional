def compute(n):
    """Complejidad O(n log n) - Tiempo Lineal-Logarítmico"""
    total = 0
    for i in range(n):
        j = n
        while j > 0:
            total += 1
            j = j // 2
    return total
