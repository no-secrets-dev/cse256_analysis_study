# Task ID: Mbpp/628

# Description/Response:
"""
Write a function to replace all spaces in the given string with '%20'.
assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'
"""
def replace_spaces(string):
    return string.replace(" ", "%20")