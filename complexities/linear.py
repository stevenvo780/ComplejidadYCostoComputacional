def compute(n):
    """O(n) - Linear time algorithm
    Execution time grows proportionally to input size"""
    total = 0
    for i in range(n):
        total += i
    return total
