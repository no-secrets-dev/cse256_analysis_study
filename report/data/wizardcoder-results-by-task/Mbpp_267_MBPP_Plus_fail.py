# Task ID: Mbpp/267

# Description/Response:
"""
Write a python function that takes in an integer n and returns the sum of the squares of the first n odd natural numbers.
assert square_Sum(2) == 10
"""
def square_Sum(n):
    sum = 0
    for i in range(1, n*2, 2):
        sum += i**2
    return sum