#Write a Python program to find the highest 3 values in a dictionary

Dict={'A':300,'B':10,'C':500,'D':600,'E':200,'F':700}
Values=sorted(Dict.values())
print("Total Values:",Values)
print("Highest 3 Values:",Values[-3::])

