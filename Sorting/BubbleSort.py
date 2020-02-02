def bubbleSort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if(list[j] > list[j+1]):
                list[j],list[j+1] = list[j+1],list[j]

list = [2,1,3,89,43,90,66]
print("Unsorted List : ",list)
bubbleSort(list)
print("Sorted List : ",list)