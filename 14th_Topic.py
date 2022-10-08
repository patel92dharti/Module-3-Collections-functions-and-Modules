#rite a Python program to get unique values from a list

List=[44,45,10,1,2,5,10,88,99,10,1,2,10,1,88]
print("Orignal Value:",List)
List=sorted(set(List))
print("Unique Value:",List)