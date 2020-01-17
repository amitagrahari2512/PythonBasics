x="Amit"
print(x)

print("Amit")

print("manage single quates and double codes in string data : use back slash (\)")
print("Amit \"Agrahari\"")


print("string type multiple times")

print("using (+) as concat")
print ("Amit"+"Amit")

print("using multiply symbol (*)")
print(5 * "Amit")

print("Amit\nAgrahari")

print("Amit\tAgrahari")

print("We want to use raw string then we need to use (r) just above the String, So it can be negate internal newLine or Tab function")

print("Negate new line")
print(r"Amit\nAgrahari")

print("Negate tab ")
print(r"Amit\tAgrahari")

fullName = "Amit"+" Agrahari"
print(fullName)

print("Get String value from index, Yes it is possible")
print("When pass positive value , it starts from 0 to last character, If pass index more than length gives an error:")
print(fullName[0])
print(fullName[12])
# print(fullName[17])

print("When pass negative value , it starts from last character to 0, If pass negative index more than length gives an error:")
print(fullName[-1])
print(fullName[-13])
#print(fullName[-14])

print("if we want multiple char the we can use name [index : no of element show index (it is exclusive)]")
print(fullName[0:3])
print(fullName[0:4])

print("If only provide index ,not provide elements show, then it will print , start to that index to end of data")
print(fullName[0:])
print(fullName[1:])

print("If only provide elements show, not provide index ,then it will print , start to provide no of element")
print(fullName[:3])

print("If we provide no of elements more than length, So we will not get any error:")
print(fullName[2:20])

print("If we provide index is negative, So we will not get any error but data is not shown")
print(fullName[-1:4])

print("If we provide index is positive, and no of elements is negative,So we will get provide index to (length-no of elements) data")
print(fullName[1:-4])

print("We can not change value of string data, because String is immutable in python")

print("find length of String")
print("length : ", len(fullName))
