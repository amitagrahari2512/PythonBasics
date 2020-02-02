print("In Linear search value can be in any order.")

pos  = -1
def linearSearch(list,searchVal):
    for data in list:
        global pos
        pos+= 1
        if(data == searchVal):
            return True
    return False

list = [2 ,10, 34, 11]
searchVal = 11

if linearSearch(list, searchVal):
    print("Found in position {}".format(pos+1))
else:
    print("Not Found")

