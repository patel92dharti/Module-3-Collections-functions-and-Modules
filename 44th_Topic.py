"""
Write a Python program to combine values in python list of dictionaries.
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':300},{'item': 'item1', 'amount': 750}]
Expected Output:
Counter ({'item1': 1150, 'item2': 300})
"""
from collections import Counter
Dict=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':300},{'item': 'item1', 'amount': 750}]
result=Counter()
for i in Dict:
    result[i['item']]+=i['amount']
print(result)
