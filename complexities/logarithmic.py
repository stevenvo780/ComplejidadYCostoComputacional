def compute(n):
    """O(log n) - Logarithmic time algorithm
    Execution time grows logarithmically with respect to n"""
    result = 0
    i = n
    while i > 0:
        result += 1
        i = i // 2
    return result
