# Task ID: Mbpp/607

# Description/Response:
"""
Write a function to search a string for a regex pattern. The function should return the matching subtring, a start index and an end index.
assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
"""
import re

def find_literals(string, pattern):
    match = re.search(pattern, string)
    if match:
        return match.group(), match.start(), match.end()
    else:
        return None, None, None