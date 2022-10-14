#Write a Python program to calculate surface volume and area of a cylinder

from math import pi

def Cylinder_Volume(radian,height):
    Surface_Volume=pi*radian*radian*height
    return Surface_Volume
def Cylinder_Area(radian,height):
    Surface_area= (2*pi*radian*radian) + (2*pi*radian*height)
    return Surface_area
Height=float(input("Enter the Cylinder Height:"))
Radian=float(input("Enter the Cylinder Radian:"))
print("Cylinder_Volume",Cylinder_Volume(Radian,Height))
print("Cylinder_Area",Cylinder_Area(Radian,Height))
