"""
Write a Python program to generate and print a list of first and last 5 elements
where the values are square of numbers between 1 and 30.
"""

def printvalue():
    l=list()
    for i in range(1,29):
        l.append(i*i)
        #l.append(i**2)
    print("First 5 Elements:-",l[:5])
    print("Last 5 Elements:-",l[-5:])
printvalue()