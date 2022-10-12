#Write a Python script to concatenate following dictionaries to create a new one.

Dict1={'A':100,'B':200,'C':300}
Dict2={10:1,20:3,30:7}
Dict3={1:"Apple",2:"Banana",3:"Manago",4:"Greps"}
Dict4={}
for i in (Dict1,Dict2,Dict3):
    Dict4.update(i)
print("Concatenate Dictionary",Dict4)
