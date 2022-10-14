#Write a Python program to calculate the area of a trapezoid

def trapezoid(base1,base2,Hight):
    area=(base1+base2/2)*Hight
    return area

Base_1=float(input("Enter base one value:"))
Base_2=float(input("Enter base two value:"))
Height=float(input("Enter Height:"))
print(trapezoid(Base_1,Base_2,Height))
