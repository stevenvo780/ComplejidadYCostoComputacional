def compute(n):
    """O(n) - Algoritmo lineal
    El tiempo de ejecución crece proporcionalmente al tamaño de entrada"""
    total = 0
    for i in range(n):
        total += i
    return total
