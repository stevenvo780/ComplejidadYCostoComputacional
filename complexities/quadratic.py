def compute(n):
    """O(n²) - Quadratic time algorithm
    Execution time grows quadratically with input size"""
    total = 0
    for i in range(n):
        for j in range(n):
            total += i + j
    return total