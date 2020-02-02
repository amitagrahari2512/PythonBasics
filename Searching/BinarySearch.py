print("In Binary search value must be sorted.")

pos  = -1
def binarySearch(list,searchVal):
    lowerBound = 0;
    upperBound = len(list)-1
    while lowerBound <= upperBound:
        mid = (lowerBound+upperBound)//2
        if(list[mid] == searchVal):
            globals()['pos'] = mid
            return True
        else:
            if(list[mid] < searchVal):
                lowerBound = mid + 1
            else:
                upperBound = mid - 1
    return False

list = [2 ,10,11, 34,67,1045]
searchVal = 1045

if binarySearch(list, searchVal):
    print("Found in position {}".format(pos+1))
else:
    print("Not Found")

