#Write a Python script to sort (ascending and descending) a dictionary by value.
import operator

d={'A': [600], 'B': [200], 'G': [20], 'C': [50],'D':[2],'E':[90]}
print("Original Dictionary:",d)
sorted_d=sorted(d.items(),key=operator.itemgetter(1))
print("Ascending sort Value:",sorted_d)
sorted_d=sorted(d.items(), key=operator.itemgetter(1),reverse=True)
print("Descending sort Value:",sorted_d)
