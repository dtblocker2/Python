def func():
    return 'hello'

greet = func

# Deleting a function
del func
try:
    print(func())
except NameError:
    print('func is deleted')

# even if func is deleted greet still works because functions areimmutable 
print(greet())

def hello():
    print('this is start if hello function')

    def greet():
        return 'this is greet inside hello'
    def welcome():
        return 'this is welcome inside hello'
    
    print(greet(),welcome())

    print('end of hello')

hello()

# welcome is in scope of function hello so we can;t call it outside
try:
    print(welcome())
except NameError:
    print('greet is not in global variable scope')


def hello(name='lol'):
    print('this is start if hello function')

    def greet():
        return 'this is greet inside hello'
    def welcome():
        return 'this is welcome inside hello'

    if name=='lol':
        return greet
    else:
        return welcome

myNewFunc = hello()

print(myNewFunc)

# now we can call greet funcion out of hello function variable scope
print(myNewFunc())

# passing a fucntion as argument
def cool():
    return 'cool'

def supercool(some_func):
    print(some_func())
    return 'super cool'

print(supercool(cool))