def fahrenheit(celsius):
    return (9 / 5) * celsius + 32


temps = [0, 22.5, 40, 100]

F_temps = map(fahrenheit, temps)

#Show
print(list(F_temps))

print(list(map(lambda x: (9/5)*x + 32, temps)))

# map() with multiple iterables
a = [1,2,3,4]
b = [5,6,7,8]
c = [9,10,11,12]

print(list(map(lambda x,y:x+y,a,b)))

# Now all three lists
print(list(map(lambda x,y,z:x+y+z,a,b,c)))



