from functools import reduce

lst =[47,11,42,13]
print (reduce(lambda x,y: x+y,lst))

max_find = lambda a,b: a if (a > b) else b

print(reduce(max_find,lst))