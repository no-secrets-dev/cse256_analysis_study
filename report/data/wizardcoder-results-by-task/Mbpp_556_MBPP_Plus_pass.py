# Task ID: Mbpp/556

# Description/Response:
"""
Write a python function to count the number of pairs whose xor value is odd.
assert find_Odd_Pair([5,4,7,2,1],5) == 6
"""
def find_Odd_Pair(arr, n):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if (arr[i]^arr[j])%2!=0:
                count += 1
    return count