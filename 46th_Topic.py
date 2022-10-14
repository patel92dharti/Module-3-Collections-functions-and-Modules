#Write a Python function to calculate the factorial of a number (a nonnegative integer)

def facN(x):
    multi = 1
    while x>1:
        multi=multi*x
        x=x-1
    return multi
n=int(input("Enter the value:"))
facN(n)
print(facN(n))
