# Task ID: Mbpp/162

# Description/Response:
"""
Write a function to calculate the sum (n - 2*i) from i=0 to n // 2, for instance n + (n-2) + (n-4)... (until n-x =< 0).
assert sum_series(6) == 12
"""
def sum_series(n):
    total = 0
    for i in range(n//2):
        total += n - 2*i
    return total