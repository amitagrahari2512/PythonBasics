print("List have provide a function called iter(listObject)")
print("Then we can use iteratorObj.__next__() method to print next value")
print("Or we can use next(iteratorObj) to print next value")

nums = [2,10,4,17]

it = iter(nums)
print("it.__next__() : ",it.__next__())
print("it.__next__() : ",it.__next__())
print("next(it) : ",next(it))


print("Iterate Through for loop")
for i in it:
    print(i)

