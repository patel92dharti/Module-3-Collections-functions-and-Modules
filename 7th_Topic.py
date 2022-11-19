#Write a Python program to check a list is empty or not.
#List=[1,2,3]
List=[]
length=len(List)
if length==0:
    print("This List is Empty now")
else:
    print("This List is not Empty.\n The Values of List: ")
    for i in List:
        print(i)
