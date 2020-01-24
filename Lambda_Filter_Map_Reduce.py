from functools import reduce

lst = [2,3,4,5,6,7,8,9,10,11,12]

print("We can use filter() method to get even no from list")

evens = list(filter(lambda a : a%2 == 0,lst))

print(evens)

print("We cam use map() function to double all even no in list")

evensDouble = list(map(lambda a : a+a,evens))
print(evensDouble)

print("I want sum of all evensDouble list, then we are using reduce() function")
print("reduce() is a part of functools library")

sum = reduce(lambda a,b : a + b , evensDouble)
print(sum)

