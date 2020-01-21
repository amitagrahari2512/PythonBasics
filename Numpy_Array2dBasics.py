from numpy import *
print("For 2d array,Python has not provide any library, So we need to install 3rd party library numpy for this")
print("through numpy we can use single dimensional array as well as multi dimensional array also")
print("we need to install library from PIP (PIP is python install manager)")
print("we need to run command on command prompt for install on idle:  python -m pip install numpy")
print("If we want to install other libraries in pycharm we need to install in pycharm with below steps:")
print("Go to file ->Settings -> projectName -> ProjectInterpreter -> click + icon -> search Numpy ->install Package")

print("We can also work for 1d array but some changes required")
#arr = array('i',[1,2,3]) it will not work with numpy,

print("Without object type specify we can call array in numpy")
arr = array([1,2,3,4])
print(arr)
print("DataType of array : arr.dtype",arr.dtype)
print("Dimension of array : arr.ndim : ",arr.ndim)

print("With object type specify we can call array in numpy")
arr = array([1,2,3,4],'i')
print(arr)

print("It we provide multitype value in array,then it will convert it all data in same type")
arr = array([1,2,3,4,6.0])
print(arr)
print("DataType of array : arr.dtype : ",arr.dtype)


arr = array([1,2,3,4,5.0,'C','AAMM',6.0])
print(arr)
print("DataType of array : arr.dtype",arr.dtype)

print("linspace(startValue,EndValue,noOfParts) function in numpy, if we not provide noOfParts then by default 50 parts generated")
arr = linspace(0,15,16)
print(arr)

arr = linspace(0,5,10)
print(arr)

arr = linspace(0,15)
print(arr)

print("logspace(startValue,EndValue,noOfParts) function in numpy, if we not provide noOfParts then by default 50 parts generated")
print("but in logspace it will show a value as (log) 10 to the power of ")
arr = logspace(0,20,5)
print(arr)

print('%.2f' %arr[0])
print('%.2f' %arr[4])

arr = logspace(0,20)
print(arr)

print("arange(startValue,endValue,steps)")
arr = arange(0,15,2)
print(arr)

print('zeros(size,type) = It will create array with zero(0)')
print('If we not provide type then byDefault float value is generated')
arr = zeros(5)
print(arr)

arr = zeros(5,int)
print(arr)

print('ones(size,type) = It will create array with one(1)')
print('If we not provide type then byDefault float value is generated')
arr = ones(5)
print(arr)

arr = ones(5,int)
print(arr)

print("We can add,subtract,multiply and division any value in array directly, without perform any operation")
arr = array([1,2,3,4,5])
arr = arr * 5
print(arr)

print("We can add,subtract,multiply and division two array directly, without perform any operation,This is called vectorized operation")
arr1 = array([1,2,3,4,5])
arr2 = array([1,2,3,4,5])
arr3 = arr1 + arr2
print(arr3)

arr = array([1,2,3,5,4])
print("we can use Trignomatry function as well")
print('sin(arr) : ',sin(arr))
print('cos(arr) : ',cos(arr))
print('tan(arr) : ',tan(arr))

print("we can use Log function as well")
print('log(arr) : ',log(arr))

print("we can use sqrt function as well")
print('sqrt(arr) : ',sqrt(arr))

print("we can use min function as well")
print('min(arr) : ',min(arr))

print("we can use max function as well")
print('max(arr) : ',max(arr))

print("we can use sum function as well")
print('sum(arr) : ',sum(arr))

print("we can sort array as well")
print('sort(arr) : ',sort(arr))

print("concat two array")
arr1 = array([1,2,3,4,5])
arr2 = array([11,12,13,14,15])
print('concatenate([arr1,arr2]) : ',concatenate([arr1,arr2]))










