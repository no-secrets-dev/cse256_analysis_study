# Task ID: Mbpp/446

# Description/Response:
"""
Write a python function to count the occurence of all elements of list in a tuple.
assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3
"""
def count_Occurrence(tup, lst):
    count = {}
    for i in lst:
        count[i] = tup.count(i)
    return count