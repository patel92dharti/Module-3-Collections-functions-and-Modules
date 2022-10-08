"""
Write a Python function that takes two lists and returns true if they have at least one common member
"""
def CommonM(a,b):
    result=False
    for i in a:
        for x in b:
            if i==x:
                result=True
                return result
    else:
        return result
print(CommonM([3,4,100,55,10,20,30],[100,40,60,80,10,1,2]))
print(CommonM([3,4,100,55],[40,60,80,10]))
