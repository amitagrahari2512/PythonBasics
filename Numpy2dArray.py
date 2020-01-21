from numpy import *

arr = array([
    [1,2,3,11,12,13],
    [4,5,6,14,15,16]
])

print("type of array arr.dtype : ",arr.dtype)
print("dimension of an array arr.ndim : ",arr.ndim)
print("rows and columns in array arr.shape : ",arr.shape)
print("Size of an array arr.size : ",arr.size)

print("convert multidimensional array to single dimensional array use flatten() function : ")
singleArr = arr.flatten()
print(singleArr)

print("convert single dimensional array to two dimensional array use reshape() function : ")
twoArr = singleArr.reshape(3,4)
print(twoArr)

print("convert single dimensional array to three dimensional array use reshape() function : ")
threeArr = singleArr.reshape(2,2,3)
print(threeArr)

print("Matrix")
arr = array([
    [1,2,3,4],
    [5,6,7,8]
])

print("convert array to matrix")
m = matrix(arr)
print(m)

print("we can direct create matrix without array also, we need to use values separated from space( ) and for row break we need to use semicolon(;)")
m = matrix('1 2 3 ; 4 5 6')
print(m)

m = matrix('1 2 ; 3 4 ; 5 6')
print(m)

m = matrix('1 2 3 ; 4 5 6 ; 7 8 9')
print(m)

print("Print diagonal element using method diagonal(m) : ",diagonal(m))
print("Print max element using method m.max() : ",m.max())
print("Print min element using method m.min() : ",m.min())

m1 = matrix('1 2 3 ; 4 5 6 ; 7 8 9')
m2 = matrix('9 8 7 ; 6 5 4 ; 3 2 1')
print("Add two matrix")
mAdd = m1 + m2
print(mAdd)

print("Subtract two matrix")
mSub = m1 - m2
print(mSub)

print("Multiply two matrix , its tough logic, but python do it own ")
mMul = m1 * m2
print(mMul)

print("divide two matrix")
mDiv = m1 / m2
print(mDiv)