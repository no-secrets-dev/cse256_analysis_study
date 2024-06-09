# Task ID: Mbpp/436

# Description/Response:
"""
Write a python function to return the negative numbers in a list.
assert neg_nos([-1,4,5,-6]) == [-1,-6]
"""
def neg_nos(lst):
    return [num for num in lst if num < 0]