def func():
    return 1
print(func())
# scope
s = 'Global Variable'
def check_for_locals():
    print(locals())

print(globals()["s"])
check_for_locals()
print(globals().keys())

def hello(name='Kiran'):
    return 'Hello '+name
print(hello())

greet = hello

print(greet)

print(greet())

del hello
# Even though we deleted the name hello, the name greet still points to our original function object. It is important to know that functions are objects that can be passed to other objects
print(greet())

