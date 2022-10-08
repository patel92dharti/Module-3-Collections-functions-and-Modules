"""
Write a Python program to count the number of strings
where the string length is 2 or more and the first and last character are same
from a given list of strings
"""
words=["abc", "xyz","aba","1221","TopT","PatelP"]
ctr=0
for i in words:
    if len(i)>1 and i[0]==i[-1]:
        ctr=1+ctr
print("Count of first and last character are same :",ctr)



