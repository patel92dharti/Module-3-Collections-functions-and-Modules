#Write a Python script to merge two Python dictionaries

Dict1={"A":2,"B":23,"D":50,"F":150}
Dict2={"A":50,"C":100,"B":"Apple","E":49,"F":500}
Dict3={}
for i in (Dict1,Dict2):
    Dict3.update(i)
print("Original Dictionary 1:",Dict1)
print("Original Dictionary 2:",Dict2)
print("Merge Dictionary:",Dict3)


