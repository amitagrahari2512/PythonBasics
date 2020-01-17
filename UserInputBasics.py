print("When we get any data from user , it datatype is string")
print("So we need to convert those datatype according to our need")

x = input()
print(type(x))
y = input()
print(type(y))
z = x+y
print(z)

print("We can provide message to getting value from user")
x = input("Enter 1st No")
print(type(x))
y = input("Enter 2nd No")
print(type(y))
z = x+y
print(z)

print("Type casting: convert string to int")
x = input("Enter 1st No")
a = int(x)
y = input("Enter 2nd No")
b = int(y)
z = a+b
print(z)

print("We convert type string just getting value from user")
x = int(input("Enter 1st No"))
y = int(input("Enter 2nd No"))
z = x+y
print(z)

print("Take character as input, but char is not a datatype in python")
x = input("Enter a value")
print(x[0])

x = input("Enter a value")[0]
print(x)

print("Evaluate a expression")

x = eval(input("Enter a expression"))
print(x)

