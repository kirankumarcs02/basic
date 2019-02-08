def hello(name='Kiran'):
    print('The hello() function has been executed')

    def greet():
        return '\t This is inside the greet() function'

    def welcome():
        return "\t This is inside the welcome() function"

    print(greet())
    print(welcome())
    print("Now we are back inside the hello() function")

hello()

# Returning Functions

def returnHello(name='Kiran'):
    def greet():
        return '\t This is inside the greet() function'

    def welcome():
        return "\t This is inside the welcome() function"

    if name == 'Kiran':
        return greet
    else:
        return welcome

x = returnHello()

print(x) # x is a greet function
print(x())

# function as a argument

def hey():
    return 'Hi Kiran!'

def other(func):
    print('Other code would go here')
    print(func())
other(hey)