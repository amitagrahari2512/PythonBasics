print("Global Variables")

a = 10

def something():
    a = 100
    print("In Function local variable a :",a)

something()
print("Outside global variable a :",a)

print("-----------------------------------")
print("I want to change global variable 'a' data inside function")
print("So for this we need to specify global just before the variable,So compiler can act this variable as global"
      "variable, and if we change any thing in that variable, it will reflect to outside variable also")

a = 10

def somethingGlobalDataChangeInsideFunction():
    global a
    a = 100
    print("In Function local variable a :",a)

somethingGlobalDataChangeInsideFunction()
print("Outside global variable a :",a)

print("---------------------------------------------")

print("But I want same name local variable and same name global variable change in a method"
      "So we need to use globals() method , and then we can change our global variable")

a = 10
print(id(a))
def somethingGlobalAndLocalVariableSameName():
    a = 20;
    print("Local variable a : ",a)
    x = globals()['a']
    print(id(x))
    print("Global variable change in function using globals()['a']=100")
    globals()['a'] = 100

somethingGlobalAndLocalVariableSameName()

print("Outside global variable a :",a)