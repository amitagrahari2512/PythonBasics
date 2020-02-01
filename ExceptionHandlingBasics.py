print("Exception have mainly two types :"
      "1 - Compile Time Exception"
      "2 - Run Time Exception")

print("We can use try , except and finally for this")
print("We can use exception overloading , with using multiple kind of errors")
print("We can use errors in any order")
print("We can use "
      "1 - try,except,finally sequence"
      "2 - try,finally sequence"
      "3 - try , except sequence"
      "4 - But we can't use try alone"
      "5 - And we can not use try,finally and except in this sequence")

print("\n----------------------------------")

a = 5
b = 0
try:
    print("Resource open")
    div = a/b
    print("Div : ",div)
    val = int(input("Enter a number"))
    print("Val : ",val)

except ZeroDivisionError as e:
    print("No can not divide by zero :", e)
except ValueError as e:
    print("Value Error  : ",e)
except Exception as e:
    print("Generic Error : ",e)

finally:
    print("Resource close")


print("\n----------------------------------")


print("\n-----------------In Any Order Exception-----------------")

a = 5
b = 0
try:
    print("Resource open")
    div = a/b
    print("Div : ",div)
    val = int(input("Enter a number"))
    print("Val : ",val)

except Exception as e:
    print("Generic Error : ",e)
except ZeroDivisionError as e:
    print("No can not divide by zero :", e)
except ValueError as e:
    print("Value Error  : ",e)

finally:
    print("Resource close")


print("\n-----------------In Any Order Exception-----------------")

print("\n-----------------Try Finally Block-----------------")

try:
    print("try")
finally:
    print("Finally")

print("\n-----------------Try Finally Block-----------------")

print("\n--------------We can not use try,finally and except order")
try:
    print("try")
finally:
    print("finally")
#except Exception e:
 #   print("Exception")
print("\n--------------We can not use try,finally and except order")


