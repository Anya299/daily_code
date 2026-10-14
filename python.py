a = [1, 2,3]
b = a

a.append(4)

print(a)
print(b)
print(a is b)
print(a == b)


a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)
print(a == b)

x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)

    inner()

outer()
print(x) 

x = "global"

def outer():
    x = "enclosing"

    def inner():
        print(x)
    def another():
        x = "another"
        inner()
    another()
    
outer()

x = 10

def change():
    #global x
    x = 20

change()

print(x)

x = "global"

def outer():
    x = "outer"

    def inner():
        nonlocal x
        #x = "changed"

    inner()
    print(x)

outer()
print(x)

x = "global"

def outer():
    x = "outer"

    def inner():
        print(x)

    def change():
        nonlocal x
        x = "changed"

    inner()
    change()
    inner()

outer()
print(x)

def modify(a, b):
    a = 100
    b.append(100)

x = 10
y = [1, 2]

modify(x, y)

print(x)
print(y)

def multiplier(n):

    def multiply(x):
        return x * n

    return multiply

triple = multiplier(3)
double = multiplier(2)

print(triple(4))
print(double(4))

def logger(func):
    def wrapper():
        print("Function started")
        func()
        print("Function finished")
    return wrapper


@logger
def hello():
    print("Hello")


hello()

def decorator(func):
    def wrapper(*args):
        print("Starting")
        result = func(*args)
        print("Result:", result)
        return result
    return wrapper


@decorator
def add(a, b):
    return a + b


x = add(3, 4)
print(x)


