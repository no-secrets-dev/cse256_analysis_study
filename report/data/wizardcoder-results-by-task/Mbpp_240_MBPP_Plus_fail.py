# Task ID: Mbpp/240

# Description/Response:
"""
Write a function that takes in two lists and replaces the last element of the first list with the elements of the second list.
assert replace_list([1, 3, 5, 7, 9, 10],[2, 4, 6, 8])==[1, 3, 5, 7, 9, 2, 4, 6, 8]
"""
def replace_list(list1, list2):
    list1[-1] = list2
    return list1