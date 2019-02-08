x = [1,2,3]
y = [4,5,6]

# Zip the lists together
print(list(zip(x,y)))

x = [1,2,3]
y = [4,5,6,7,8]

# Zip the lists together
print(list(zip(x,y)))


# dictionaries
d1 = {'a':1,'b':2}
d2 = {'c':4,'d':5}

print (list(zip(d1,d2)))

print(list(zip(d2,d1.values())))

# switch the keys and values of the two dictionaries:

def switcharoo(d1, d2):
    dout = {}

    for d1key, d2val in zip(d1, d2.values()):
        dout[d1key] = d2val

    return dout



print(switcharoo(d1,d2))

