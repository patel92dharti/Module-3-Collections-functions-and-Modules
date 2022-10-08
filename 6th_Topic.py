#Write a Python program to remove duplicates from a list.
List =[100,10,50,6,2,0,45,42,42,100,63,0,45,10,50]
print("Orignal List: ",List)
List=sorted(set(List))
print("After Duplicate Remove List:",List)
