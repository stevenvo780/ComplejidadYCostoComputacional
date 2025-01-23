def compute(n):
    """O(log n) - Algoritmo logarítmico
    El tiempo de ejecución crece de manera logarítmica con respecto a n"""
    result = 0
    i = n
    while i > 0:
        result += 1
        i = i // 2
    return result
