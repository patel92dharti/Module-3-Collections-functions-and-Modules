#Write a Python program to remove an empty tuple(s) from a list of tuples.

List=[(),(),(0 , ),(),(),(),('True','False'),(400,4),(2,3),(5,4),(8,1)]

for i in List:
    if i == ():
        List.remove(())
        print(List)
        continue
#List = [t for t in List if t]

print(List)



