#Write a Python program to reverse a tuple.
Tuple=('A','b','c',"Dharti",22,33,33,41,4,1,100)
print("Orignal Value:",Tuple)
Tuple=tuple(reversed(Tuple))
print("Reverse Value",Tuple)

Tuple=Tuple[::-1]
print(Tuple)
Tuple=Tuple[::-1]
print(Tuple)