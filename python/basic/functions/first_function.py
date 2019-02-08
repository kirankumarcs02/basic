def name_function():
    '''
    DOCSTRING : information about the function
    :return:
    '''
    print('hello')


name_function()

def say_hello(name):
    print('hello   '+ name)

say_hello('kiran')

# first return

def first_return(name = 'name'):
    return 'Hey '+ name

result = first_return('Kiran')

print(result)


# args

def myFunc(*args):
    return sum(args)
res = myFunc(1,2,3,4,5)
print(res)


# key word args

def myKeyWordFun(**kwargs):
    print(kwargs)
    if 'key' in kwargs:
        return "key is present"
    else:
        return 'No key'

result = myKeyWordFun(key = 1, num=2)
print(result)
