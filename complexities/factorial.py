def compute(n):
    """O(n!) - Factorial time algorithm
    Execution time grows factorially with input size"""
    if n <= 1:
        return 1
    total = 0
    for _ in range(n):
        total += compute(n-1)
    return total
