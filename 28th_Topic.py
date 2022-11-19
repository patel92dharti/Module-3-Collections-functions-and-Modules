#Write a Python program to convert a list of tuples into a dictionary.

L=[("A",100),("B",200),("A",500),("A",600),("G",20),("C",10),("C",50)]
d={}
for x,y in L:
    d.setdefault(x,[]).append(y)
print(d)
print(d.keys())
print(d.get("B"))
print(d.setdefault("D",[400]))
print(d)
print(d.fromkeys("B",[14]))
print(d)
print(d.__len__())
