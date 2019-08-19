width = 17
height = 12.0
delimiter = '.'

print (width/2 )
print (width/2.0)
print (height/3)
print (1+2*4)
print (delimiter * 5)

#  4/3 pi r3

print( 4 * 3.412 * (5**3)/3)

x = 6

def example2():
    # works
    print(x)
    print(x+5)

    # but then what happens when we go to modify:
    # x+=6

example2()

test = 'akk'
print(test[2:0:-1])
print("test = ", test[1::-1] == test[0:])