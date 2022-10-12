#Write a Python program to check whether a list contains a sub list

List=[["Apple","Banana","Mango"],[1,2,3,4,5,6],'A','B','C',"Tops",[100,200,300],500,[0.0,0.1,0.2,0.3]]
for i in List:
    Type=type(i)
    if Type==list:
        Sub_List=list(i)
        print("Its Sub List:",Sub_List)


