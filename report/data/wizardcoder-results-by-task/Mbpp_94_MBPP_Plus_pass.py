# Task ID: Mbpp/94

# Description/Response:
"""
Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
"""
def index_minimum(lst):
    return min(lst, key=lambda x: x[1])[0]