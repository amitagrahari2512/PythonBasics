
print("When we want to do programming with file system"
      "we need to use open(fileName, mode)"
      "mode represents read,write etc")

print("Basically wehen we work on data , it is working on two types"
      "1 - character (like any file or character)"
      "2 - binary (Like image,binary)")

print("If we want to write a file,we need to use differnt mode"
      "mode w - it can write gdata in file, but when we again run code then "
      "it delete earlier value and then write current data"
      "mode a - it will append data in file, it cannot delete older data from file")

print("If we work on image or any binary file , we need to use mode as , (wb,rb)")

print("\n Reading a file")
file = open('File','r')

print("fileObject : ",file)

print("\nwhen we want to read all file content then use read() method")
print(file.read())
print("After reading data from read() method , we can not read data again, because it automatically"
      "reach their end point")
print("\n------------------------------------------------------------")

print("\n when we want to read data in line by line , then we can use readline() method")
file = open('File','r')
print(file.readline())
print(file.readline())
print("\n----------------------------------------------------------------------------")

print("\n when we want some character from line then we can use readline(noOfCharacter)")
print("If noOfCharacter is lessThan current size of content in line, then nextline() is always sameLine but except provided character"
      "if noOfCharacter is equals+1 current size of content in line, then nextline() is always nextline() of file")
print(file.readline(3))
print(file.readline())

print("\n----------------------------------------------------------------------------")

print("use readlines(hint) method for get lines as per provided byte size")
print("hint : Optional. If the number of bytes returned exceed the hint number, "
      "no more lines will be returned. Default value is  -1, "
      "which means all lines will be returned.")
file = open('File','r')
print(file.readlines(50))
print("\n----------------------------------------------------------------------------")