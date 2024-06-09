# Task ID: Mbpp/287

# Description/Response:
"""
Write a python function takes in an integer n and returns the sum of squares of first n even natural numbers.
assert square_Sum(2) == 20
"""
def square_Sum(n):
    sum = 0
    for i in range(1, n+1, 2):
        sum += i**2
    return sum