print("If we want to write a file,we need to use differnt mode"
      "mode w - it can write gdata in file, but when we again run code then "
      "it delete earlier value and then write current data"
      "mode a - it will append data in file, it cannot delete older data from file")

print("If we work on image or any binary file , we need to use mode as , (wb,rb)")

#file = open("writeFile",'w')
#file.write("Write mode data")

#file = open("writeFile",'a')
#file.write("Append mode data")

print("\n I want to write all data from file 'file.txt' to 'writeFile.txt'")

file = open('file','r')
fileWrite = open('writeFile','w')

for data in file:
      fileWrite.write(data)


print("\n working with image or binary data ,")
readImage = open('PythonType_Size_Image.PNG','rb')

for data in readImage:
      print(data)

print("\nRead one image and write in another file")

readImage = open('PythonType_Size_Image.PNG','rb')
writeImage = open('PythonType_Size_Image_copy.PNG','wb')

for data in readImage:
      writeImage.write(data)

