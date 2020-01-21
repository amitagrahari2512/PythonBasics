from numpy import *
print("Copy of array")
arr1 = array([1,2,3,4,5])
arr2 = arr1

print(arr1)
print(arr2)

print("Both address is same")
print(id(arr1))
print(id(arr2))

print("------------------------------Shallow Copy------------------------------------------------")

print("So we can use view() method , so it will gives new address, But this is shallow Copy")
arr1 = array([1,2,3,4,5])
arr2 = arr1.view()
print(arr1)
print(arr2)

print("Both address is different")
print(id(arr1))
print(id(arr2))

print("But this is a shallow copy, means if I change any value in arr1 it will reflect to arr2 as well")
arr1[1] = 100
print(arr1)
print(arr2)
print("------------------------------------------------------------------------------")

print("------------------------------Deep Copy------------------------------------------------")

print("So if we don't want this , we need to use copy() function, so it will create deep copy of array")
print("so in this time actual array and copy Array are not interlinked")
arr1 = array([1,2,3,4,5])
arr2 = arr1.copy()
print(arr1)
print(arr2)

print("Both address is different")
print(id(arr1))
print(id(arr2))

print("But this is a deep copy, means if I change any value in arr1 it will not reflect to arr2")
arr1[1] = 100
print(arr1)
print(arr2)

print("------------------------------------------------------------------------------")


