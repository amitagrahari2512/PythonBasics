a = 5
b = 6

temp = a
a = b
b = temp

print(a)
print(b)

a = 5
b = 6

a = a+b
b = a-b
a = a-b

print(a)
print(b)

print("using xor concept")
a = 5
b = 6

a = a ^ b
b = a ^ b
a = a ^ b

print(a)
print(b)

print("using python 2nd rotation concept")
print("It use stach concept a,b = b,a . First right side value put in stack and then it will rotate the stack two value and then assign value.")
print("This item called Rot_Two concept in python,We can get more info from this link")
print("https://docs.python.org/3/library/dis.html#opcode-ROT_TWO")
a = 5
b = 6

a,b = b,a
print(a)
print(b)