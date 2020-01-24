def square(x):
    return x*x

print(square(5))

print("Create Square function using lambda : ")

sq = lambda a : a*a

print("Called Lambda function : ")
result = sq(5)
print(result)

print("Sum of two no with lambda : ")
sum = lambda a , b : a+b
result = sum(2,5)
print(result)
