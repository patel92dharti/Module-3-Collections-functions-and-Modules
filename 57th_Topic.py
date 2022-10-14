#Write a Python program to convert degree to radian
from math import pi

def degrees_radian(degrees):
    return degrees*pi/180.0

print(degrees_radian(float(input("Enter Degree:"))))
