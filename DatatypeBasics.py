print("There are many types of datatypes.")
print("NONE-when not declare anything to variable, then none called")
print("Numeric - Int,Float,complex,bool")
print("List")
print("Tuple")
print("Set")
print("String")
print("Range")
print("List,Tuple,Set,String and range are part of sequence")
print("Map or Dictionary")

print("Example of Numeric")
num = 2.5
print(type(num))

num = 5
print(type(num))

print("For complex no use : a + bj format where j is mandatory for complex")
num = 6 + 9j
print(type(num))

print("convert float to int")
num = 8.5
a = int(num)
print(a)

print("convert int to float")
num = float(a)
print(num)

print("create complex no, use a+bj")
a = 3
b = 6
c = complex(3,6)
print(c)

print("Boolean type")
boolVal = a<b
print(boolVal)
print(type(boolVal))

print("Convert bool type to int")
print("True as : ",int(True))
print("False as : ",int(False))

print("list type")
l = [10,20,30,40]
print(l)
print(type(l))

print("Set type")
s = {10,20,30,40}
print(s)
print(type(s))

print("Tuple type")
t = (10,20,30,40)
print(t)
print(type(t))

print("String type,Python does not have char type,we can consider single character string as a char")
str = 'Amit'
print(str)
print(type(str))

str = 'A'
print(str)
print(type(str))


print("Range type")
print(range(10))
print("List of range : " , list(range(10)))
print("List of even no :range (start,end,difference)" , list(range(2,10,2)))
print("type : ", type(range(10)))

print("maps or list")
d = {"Amit":"onePlus","Himanshu":"Moto","AmitB":"MI"}
print(d)
print("type : ", type(d))
print("keys in dictionary : ", d.keys())
print("values in dictionary ; ", d.values())
print("Get data from [key] : ",d["Amit"])
print("Get data from get(key) method : ", d.get("Amit"))