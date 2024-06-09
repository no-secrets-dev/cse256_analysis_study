# Task ID: Mbpp/603

# Description/Response:
"""
Write a function to get all lucid numbers smaller than or equal to a given integer.
assert get_ludic(10) == [1, 2, 3, 5, 7]
"""
def get_ludic(n):
    """
    Returns a list of all lucid numbers smaller than or equal to n.
    """
    lucid = []
    for i in range(1, n+1):
        if sum(i for i in range(1, int(i**0.5)+1) if i%i == 0) + i**2 == i*(i+1)//2:
            lucid.append(i)
    return lucid