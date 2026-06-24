## Functions
def is_even(num):
    """
    this fuction returns if a given number is odd and even
    """
    if num % 2==0:
        return 'even'
    else:
        return 'odd'
# for i in range(1,11):
#     x = is_even(i)
#     print(x)

## Types of arguments:
# 1. default argument :
def greet(a=1,b=3):
    return a * b
# print(greet(34,22))
# print(greet(34))

# 2. Positional Arguments:
def student(name, age):
    print("Name:", name)
    print("Age:", age)
# student("ajay",34)
# student(32,"ajay") # ambiguity happens

# 3. Keyword Arguments:
def student(name, age):
    print("Name:", name)
    print("Age:", age)
# student(age=23,name="sujay")
# student(name="sujay",age=54)

## *args
def multiply(*args):
    products = 1
    for i in args:
        products = products * i
    return products
# print(multiply(1,2,3,4,5,6))
# print(multiply(1,2,3,4,5,6,8,9,11,21,32,12))

# how to access doc
# print(print.__doc__)

# ** kwargs
def display(**kwargs):
    for (key,value) in kwargs.items():
        print(key,'->',value)
# display(india='delhi',srilanka='columbo')


## variable scope
# def geek(y):
#     print(x)
#     print(x + 1)
# x =5
# geek(x)
# print(x)

## nested function
def f():
    def g():
        print("inside func g")
    g()
    print("inside func f")
# g() # error






