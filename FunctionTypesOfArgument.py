print("Their are two types of Argument")
print("1 - Formal Argument (Which is use in creating a function)")
print("2 - Actual Argument (Which is passed by user at a time of function calling)"
      "Actual Arguments have four types : "
      "(1)Position"
      "(2)Keyword"
      "(3)Default"
      "(4)Variable Length"
      "(5)Keyword Variable Length")

def add(a,b): #There a and b are formal arguments
    c = a+b
    print(c)

add(2,3) # There 2 and 3 are Actual Arguments

print("position Argument Type")
print("If we know the sequence of argument type,Then we can use position")
def person(name,age):
    print(name)
    print(age)

person("Amit",29)

print("Keyword Argument type")
print("If we don't know the sequence of argument, but we know argument name of this method"
      "Then we can use name of Argument with value")

def person(name,age):
    print(name)
    print(age)

person(age=29,name="Amit")

print("If we not provide formal argument name in keyword, then we will get error like person(xx=1,zz=A),"
      "becaus ein person xx and zz is not a formal argument")

print("Default Argument Type")
print("Sometimes we declare some default value in formal argument, So if user don't provide data in that argument,default value is use")

def personDefault(name,age=18):
    print(name)
    print(age)

personDefault("amit",29)
personDefault("amit")

print("variable length argument :")
print("For variable length we need to use *VariableName and this variableName is considered as a tuple")
print("We can use variable length always be a last argument in method like sum(a,*b),"
      "otherwise we will get error")
def sum(a,*b):
    print(a)
    print(b)
    c =a;
    for i in b:
        c = c + i

    print("sum = ",c)

sum(5,5,5,5,5)

def sum(*b):
    print("OnlyVariable Length")
    print(b)
    c =0;
    for i in b:
        c = c + i

    print("sum = ",c)

sum(5,5,5,5,5)

print("error if we use variable length from that type : multipleVal(*a,b)")
#def multipleVal(*a,b):
#   print(a)
#   print(b)

#multipleVal(1,2,3,4,5.0)

print("Keyword Variable Length")
print("Sometimes user wants to insert data with some keys , So we can identify in our method, the value where it belongs")
print("for this we need to use **variable at the end of the formal parameters")

def keywordWithVariableLength(name,**data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,":",j)

keywordWithVariableLength("Amit",age=29,qualification="Btech")







