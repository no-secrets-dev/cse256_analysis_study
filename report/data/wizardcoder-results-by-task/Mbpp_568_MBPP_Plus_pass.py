# Task ID: Mbpp/568

# Description/Response:
"""
Write a function to create a list of N empty dictionaries.
assert empty_list(5)==[{},{},{},{},{}]
"""
def empty_list(n):
    return [{} for i in range(n)]