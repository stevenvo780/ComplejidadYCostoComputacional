
def compute(n):
    """Complejidad O(n²) - Tiempo Cuadrático"""
    total = 0
    for i in range(n):
        for j in range(n):
            total += i + j
    return total