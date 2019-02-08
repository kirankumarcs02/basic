def myfunc(x):
    return [num for num in range(x) if num%2==0]
myArray = myfunc(10)

print(myArray)