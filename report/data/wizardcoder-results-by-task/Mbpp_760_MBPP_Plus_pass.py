# Task ID: Mbpp/760

# Description/Response:
"""
Write a python function to check whether a list of numbers contains only one distinct element or not.
assert unique_Element([1,1,1]) == True
"""
def unique_Element(lst):
    return len(set(lst)) == 1