#Write a Python program to unzip a list of tuples into individual lists.

L=[2,4,5,6,(23,52.3,90,85,96),45,(78,True,False),("Tops","File","Dharti")]

print("Main List:",L)
for i in L:
    Type=type(i)
    #print(Type)
    if Type==tuple:
        Individual_List=list(i)
        print("Individual List:",Individual_List)


