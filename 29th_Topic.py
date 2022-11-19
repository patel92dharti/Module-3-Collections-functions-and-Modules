#How will you create a dictionary using tuples in python?
"""
In Python, use the dict() function to convert a tuple to a dictionary.
A dictionary object can be created with the dict() function.
The dictionary is returned by the dict() method, which takes a tuple of tuples as an argument.
A key-value pair is contained in each tuple.
"""
L=(("A",100),("B",200),("A",500),("A",600),("G",20),("C",10),("C",50))
d={}
#resultDictionary=dict((x,y) for x,y in L)
#print(resultDictionary)
for a,b in L:
    d.setdefault(a,[]).append(b)
print(d)
