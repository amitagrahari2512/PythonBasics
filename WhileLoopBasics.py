print("When we want after print we will not get data in new line, We need to use , end="" at the end of print");
print("The value we written in end , It will be print after after each print statement")

i = 0;
while i<5:
    print("While")
    i=i+1

print("loop Done")

print("Use nested while loops")

x = 0
while x < 5:
    print("While ",end="")
    y = 0
    while y < 3:
        print("Nested",end=" ")
        y = y+1
    x=x+1
    print()
