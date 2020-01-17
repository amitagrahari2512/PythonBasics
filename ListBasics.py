print("List is mutable,\n it declared with the help of [] brackets")

nums = [20, 30, 40, 50]

print(nums)

print("find no with positive index : ")
print(nums[0])
print(nums[1])
print(nums[3])

print("find no with negative index : ")
print(nums[-4])
print(nums[-3])
print(nums[-1])

print("we can get all data with positive index [startIndex:no of element show index(it is exclusive)]")
print(nums[0:])
print(nums[1:])
print(nums[0:3])
print(nums[1:2])

names = ["amit" , "abhi" , "anu"]
print(names)

print("In Pythin list can have mutiple variable data, like,integer,float and string also :")
multiTypeValueList = [9, 9.5 , "Amit"]
print(multiTypeValueList)

print("list of list with multiple types")
mixList = [nums , names, multiTypeValueList]
print(mixList)

print("List Function - List is mutable so we can change values")
print("Append(value) - it insert data in end")
nums.append(45)
print(nums)

print("Insert(index,value) - it insert data in between")
nums.insert(1,12)
print(nums)

print("remove(value) - it remove specify value from list")
nums.remove(30)
print(nums)

print("pop(index) : it will remove data with the help of index, if index not provided it will delete last insert value in it.")
nums.pop(3)
print(nums)

print(nums.pop())

print("delete multiple values use del list[startIndex:endIndex(exclusive)]")
del nums[1:]
print(nums)

nums.append(1)
nums.append(2)
nums.append(3)
nums.append(4)
nums.append(5)

print(nums)

del nums[2:5]
print(nums)

print("We can add multiple values in list using extend() command")
nums.extend([10,100,1000])
print(nums)

print("in built function")
print("min : ", min(nums))
print("max : ", max(nums))
print("sum : ", sum(nums))

print("Sort in list using sort() method")
nums.sort()
print(nums)