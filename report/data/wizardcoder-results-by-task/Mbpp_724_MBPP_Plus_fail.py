# Task ID: Mbpp/724

# Description/Response:
"""
Write a function that takes base and power as arguments and calculate the sum of all digits of the base to the specified power.
assert power_base_sum(2,100)==115
"""
def power_base_sum(base, power):
    result = 0
    for i in range(power):
        result += base
    return result