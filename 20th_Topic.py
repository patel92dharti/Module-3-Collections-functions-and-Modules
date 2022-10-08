#Write a Python program to check whether an element exists within a tuple.

Tuple=(44,5,1,2,66,99,55,22,True,False,55.5)
Ele=int(input("Enter Value: "))
for i in Tuple:
    if i==Ele:
        print("Already Exists")
        break
else:
    print("Not in Tuple")



