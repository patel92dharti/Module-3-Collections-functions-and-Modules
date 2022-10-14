#Write a Python function to check whether a number is in a given range

def ranage_Fun():
    X = int(input("Enter Number"))
    for i in range(1,30):
        if i==X:
            print("Your given number is in range")
            break
    else:
        print("your given number is out of range")
ranage_Fun()