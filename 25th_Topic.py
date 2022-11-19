#Write a Python program to find the repeated items of a tuple.

Tuple=('A','b','c',"Dharti",22,33,33,41,4,1,100,True,False,33,11,1,1,2)
print(Tuple)
Count=Tuple.count(True)
print("Repeated Item Count:-",Count)

MainTuple=(22,33,33,41,4,1,100,33,11,1,1,2)
FOund_Item=[]
Repeated_item=[]
for i in range(len(MainTuple)):
    if MainTuple[i] in FOund_Item:
        Repeated_item.append({
            "Index": i,
            "Value": MainTuple[i]

        })
    else:
        FOund_Item.append(MainTuple[i])

print(Repeated_item)



