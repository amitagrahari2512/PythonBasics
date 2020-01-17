print("Tuple is immutable,\n Tuple declared with () brackets,\ntuples data can not be change")

tup = (10, 20, 30, 40, 40)
print(tup)

print(tup[0])
print(tup[0:])
print(tup[0:2])
print(tup[:-2])

print("tuple index method, search the index of provided value in tuple, if value not present then gives valueError")
print(tup.index(10))
#print(tup.index(50)) #Error Throw

print("tuple count method , count no of occurance of provided value in tuple")
print(tup.count(40))
print(tup.count(5))




