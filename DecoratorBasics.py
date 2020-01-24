import math
print("Decorator can add extra feature to the existing function : ")
print("With decorator we can change the existing behaviour of the current function")
print("I have div(a,b) function which can divide, but i want when numerator is less than denominator,"
      "we can swap no but we cannot change anything in div(a,b) function")

print("Imp : In python we can pass function in a parameter")

print("Inner function always be a same parameter a function passed in decorator")

def div(a,b):
    print(a/b)


def smart_div(func):

    def inner(a,b):
        if a<b:
            a,b = b,a
            return func(a,b)

    return inner

div1 = smart_div(div)
div1(2,4)

print("Or we can use same method name, their is no problem in this")
div = smart_div(div)
div(2,4)

print("Using decorator chnage name")
def name(n):
    print(n)

def smart_name(func):
    def inner(n):
        n = n + "AAAAAA"
        return func(n)

    return inner

name = smart_name(name)
name("Amit")

print("We will call trignomatry function using decorators")

def foo(func):
    res = 0
    for x in [1, 2, 2.5]:
        res += func(x)
    return res

print(foo(math.sin))
print(foo(math.cos))

print("---------------fooWithList------------------")

def fooWithList(func,lst):
    res = 0
    for x in lst:
        res += func(x)
    return res

lst = [1, 2, 2.5]
print(fooWithList(math.sin,lst))
print(fooWithList(math.cos,lst))
