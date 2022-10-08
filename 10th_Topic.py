"""
Write a Python function that takes a list and returns a new list
with unique elements of the first list.
"""
def uniquelist(a):
    l=[]
    for i in a:
        if i not in l:
            l.append(i)
    return l
print("New List:",uniquelist([1,2,3,3,3,4,4,5,6,5,6,6,7,1,8,9,11]))
