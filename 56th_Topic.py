#Write a Python program to read a random line from a file.

import random
with open("data1.txt","r") as file:
    allText=file.read()
    Lines=list(map(str,allText.splitlines()))
    print(random.choice(Lines))

def fileope(datafile):
    data22 = open("data2.txt", "r")
    allt=data22.read().splitlines()
    return random.choice(allt)

print(fileope("data2.txt"))





