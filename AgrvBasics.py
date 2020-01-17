import sys
print("in argv we can get multiple values which one provide from user ")
print("in cmd :python fileName 1 2 ")
print("index 0 is file name,index 1 is 1 and index 2 is 2, but values in string format")
print("argv is part of sys module")
x = int(sys.argv[1])
y = int(sys.argv[2])
z =x + y
print(z)
