"""
Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string: 'w3resource'
Expected output:
{'3': 1,āsā: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
"""
S="w3resourcew3resourcew3resource"
Dict={}
for l in S:
    Dict[l]=Dict.get(l,0)+1
print(Dict)

