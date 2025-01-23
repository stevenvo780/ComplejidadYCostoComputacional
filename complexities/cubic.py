def compute(n):
    """O(n³) - Cubic time algorithm
    Execution time grows cubically with input size"""
    total = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                total += i + j + k
    return total
