print("Python is not call by value and not call by refernce")
print("Correctly speaking, Python uses a mechanism, which is known as \"Call-by-Object\", sometimes also called \"Call by Object Reference\" or \"Call by Sharing\"")

print("If we pass immutable object (like int , string etc) its internally "
      "create new object when we assigned any value,so address is diffrent"
      "And pass object does not change.")
print("Argument as Immutable type")

def methodArgAsImmutable(x):
    print("Inside Method")
    print("x = : ",x ,"id = :",id(x))
    x = 90;
    print("x = : ", x, "id = :", id(x))
    print("Inside Method")

print("Call methodArgAsImmutable()")
x = 10
print("Before call method methodArgAsImmutable() x = : ",x ,"id = :",id(x))
methodArgAsImmutable(x)
print("After call method methodArgAsImmutable() x = : ",x ,"id = :",id(x))

print('\n')

print("If we pass mutable object (like List , Obj etc) its assigned value in particular object, and address is same,"
      "So that's why pass values has been change itself.")
print("Argument as mutable type")

def methodArgAsMutable(lst):
    print("lst = : ",lst ,"id = :",id(lst))
    lst[3] = 90;
    print("lst = : ", lst, "id = :", id(lst))

print("Call methodArgAsMutable()")
lst = [1,2,3,4,5,6]
print("Before call method methodArgAsMutable() lst = : ",lst ,"id = :",id(lst))
methodArgAsMutable(lst)
print("After call method methodArgAsMutable() lst = : ",lst ,"id = :",id(lst))
