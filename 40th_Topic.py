#Write a Python program to print all unique values in a dictionary.

Dict={'A':200,'B':500,'C':500,'D':"User1",'F':"User1",'E':100,'G':200}
List=[]
for Value in Dict.values():
    if Value not in List:
        List.append(Value)
    else:
        continue
print("Unique Values:",List)
