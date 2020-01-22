def greet():
    print("hello")
    print("Congrats for creating first function")

print("Call greet() function")
greet()

def add(a,b):
    c = a+b
    print(c)

print("Call add() function")
add(2,4)

print("create function with return value")
def addReturn(a,b):
    c = a+b
    return c

print("call addReturn() method")
addReturn(2,3)

print("Create function with multiple return value")
def add_sub_multiple_return(a,b):
    add =a+b
    sub=a-b
    return add,sub

print("call add_sub_multiple_return() method")
returnAdd,returnSub = add_sub_multiple_return(2,4)
print(returnAdd,returnSub)



