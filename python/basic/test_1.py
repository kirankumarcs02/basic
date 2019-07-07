def pyfunc(r):
    for x in range(r):
        print(' '*(r-x-1)+'*'*(2*x+1))

pyfunc(3)
print('-------------------------------------')
def pyfuncRev(r):
    for x in range(r):
        print(' '*(r-(r-x))+'*'*(2*(r-x-1)+1))

pyfuncRev(3)