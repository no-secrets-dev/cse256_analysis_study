# Task ID: Mbpp/105

# Description/Response:
"""
Write a python function to count true booleans in the given list.
assert count([True,False,True]) == 2
"""
def count_true(lst):
    count = 0
    for item in lst:
        if item:
            count += 1
    return count