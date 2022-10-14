#Write a Python function to check whether a number is perfect or not.
#Divisor of 28 :1,2,4,7,14,28
#sum of 1+2+4+7+14=28
#sum=original number
def perfect_Num(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    return sum==n

print(perfect_Num(int(input("Enter the number:"))))