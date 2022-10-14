#Write a Python program to calculate the area of a parallelogram

def parallflelogram(base,height):
    Area=base*height
    return Area

Base=float(input("Enter Base length:"))
Height=float(input("Enter Height:"))
print(parallflelogram(Base,Height))