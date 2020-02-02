def selectionSort(list):
    for i in range(len(list)-1):
        minPos = i
        for j in range(i,len(list)):
            if(list[j] < list[minPos]):
                minPos = j

        #Swap Values
        list[i],list[minPos] = list[minPos],list[i]


list = [2,1,3,89,43,90,66]
print("Unsorted List : ",list)
selectionSort(list)
print("Sorted List : ",list)