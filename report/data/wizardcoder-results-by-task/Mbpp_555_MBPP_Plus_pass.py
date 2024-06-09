# Task ID: Mbpp/555

# Description/Response:
"""
Write a python function to find the difference between the sum of cubes of the first n natural numbers and the sum of the first n natural numbers.
assert difference(3) == 30
"""
def difference(n):
    sum_of_cubes = sum([i**3 for i in range(1, n+1)])
    sum_of_numbers = sum(range(1, n+1))
    return sum_of_cubes - sum_of_numbers