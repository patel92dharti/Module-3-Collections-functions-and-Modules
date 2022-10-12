#Write a Python program to check multiple keys exists in a dictionary

Dict={5: 100, 6: 200, 7: 300, 10: 1, 20: 3, 30: 7, 1: 'Apple', 2: 'Banana', 3: 'Manago', 4: 'Greps'}

print(Dict.keys()>={'Apple',4})
print(Dict.keys()>={5,6})
print(Dict.keys()>={'Banana','Manago'})
print(Dict.keys()>={7,20})

