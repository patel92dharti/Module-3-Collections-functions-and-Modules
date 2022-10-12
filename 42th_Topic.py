"""
Write a Python program to create and display all combinations of letters,
selecting each letter from a different key in a dictionary.
Sample data: {'1': ['a','b'], '2': ['c','d']}
Expected Output:
ac ad bc bd
"""
import itertools
Dict={'1':['a','b'],'2':['d','c'],'3':['e','f']}
for Combi in itertools.product(*[Dict[k] for k in sorted(Dict.keys())]):
    print(''.join(Combi))

