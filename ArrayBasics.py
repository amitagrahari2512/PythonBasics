from array import *

print("We can describe array with method array(type,values)")

vals = array('i',[1,5,6,8,-9]);
print('Array : ',vals)
print('Type of array use typecode',vals.typecode)
print('Array Info buffer_info(), It will return (address,size): ',vals.buffer_info())
print('Use index in Array vals[0] : ',vals[0])
print("get length of array : ",len(vals))
print("Add data in end position : ")
vals.append(500)
print("After Add data in end position : ",vals)
print("insert data in particular position:")
vals[2] = 100
print("After insert array : ",vals)

print("Print All data of array")
for i in range(5):
    print(vals[i])

print("Print All data of array with help of length")
for i in range(len(vals)):
    print(vals[i])

print("Print All data of array with help of array values")
for i in vals:
    print(i)

print("Copy Of existing array")
newArray = array(vals.typecode,(a for a in vals))
print("values of new array")
for i in newArray:
    print(i)

print("Copy Of existing array: and get values as a square root")
newArray = array(vals.typecode,(a*a for a in vals))
print("values of new array")
for i in newArray:
    print(i)

print('Reverse the array :')
vals.reverse()
print("Reverse array : ",vals)

print("use unsigned array")
#vals = array('I',[1,-2,3,4,5]) We cannot use negative no in unsigned array.
vals = array('I',[1,2,3,4,5])
print("Unsigned int array : ",vals)

print('Use character array')
vals = array('u',['a','b','c'])
for i in vals:
    print(i)

print("---------------------------------User Input for create array-----------")
userArr = array('i',[])
arrLength = int(input("Enter Size of array"))
for x in range(arrLength):
    val = int(input("Enter next value"))
    userArr.append(val)

print("use input array : ",userArr)

print('search value in User array')
searchVal = int(input("which no index want to search"))

index = 0
for i in userArr:
    if i == searchVal:
        print("index : ",index)
        break

    index+=1

print("Search value index from array index(searchVal) method. "
      "If search element not found in array so throw error message."
      "It we have sear value no multiple times,then it can find index of first search value")
print("index : ",userArr.index(searchVal))




