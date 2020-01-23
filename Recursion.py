import sys
print("In Pythin default recursion limit is 1000, "
      "If we want to change this limit we can change it.")

print("Recursion Limit : ",sys.getrecursionlimit())
sys.setrecursionlimit(2000)
print("Recursion Limit after change : ",sys.getrecursionlimit())

print("Factorial using recurssion :")

def factUsingRecursion(n):
    if n == 0:
        return 1
    return n*factUsingRecursion(n-1)

print(factUsingRecursion(5))