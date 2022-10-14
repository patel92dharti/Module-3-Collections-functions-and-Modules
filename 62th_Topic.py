#Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.
from decimal import *
data=list(map(Decimal,'2.45 2.2 0.01 4.5 0.2 6.52 8.25 0.30 0.90'.split()))
print("Total Decimal Number:",data)
print("Maximum Decimal Number:",max(data))
print("Minimum Decimal Number:",min(data))
