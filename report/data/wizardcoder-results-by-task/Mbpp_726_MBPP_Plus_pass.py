# Task ID: Mbpp/726

# Description/Response:
"""
Write a function that takes as input a tuple of numbers (t_1,...,t_{N+1}) and returns a tuple of length N where the i-th element of the tuple is equal to t_i * t_{i+1}.
assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)
"""
def multiply_elements(t):
    result = []
    for i in range(len(t)-1):
        result.append(t[i] * t[i+1])
    return tuple(result)