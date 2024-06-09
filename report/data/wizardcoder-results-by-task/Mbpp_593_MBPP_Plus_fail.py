# Task ID: Mbpp/593

# Description/Response:
"""
Write a function to remove leading zeroes from an ip address.
assert removezero_ip("216.08.094.196")==('216.8.94.196')
"""
def removezero_ip(ip):
    return ".".join(str(int(i)) for i in ip.split("."))