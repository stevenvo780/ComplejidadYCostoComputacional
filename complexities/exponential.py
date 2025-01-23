def compute(n):
    """O(2ⁿ) - Exponential time algorithm
    Execution time doubles with each unit increase in input"""
    if n <= 1:
        return n
    return compute(n-1) + compute(n-2)
