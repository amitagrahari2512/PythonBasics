print("Zip Funtion in python is use for concate two list, set or tuple")

nameTuple = ("Amit" , "Abhi", "Vinay", "Amit")
workTuple = ("Job", "Study" , "Business", "Job")

zippedList = list(zip(nameTuple,workTuple))
print("zippedList = ",zippedList)

zippedSet = set(zip(nameTuple,workTuple))
print("zippedSet = ",zippedSet)

zippedDict = dict(zip(nameTuple,workTuple))
print("zippedDict = ",zippedDict)

print("-----------When we haven't same no of list--------")
print("Then it will zip only those values have corresponding value in other collections")
nameTuple = ("Amit" , "Abhi", "Vinay")
workTuple = ("Job", "Study" )

zippedList = list(zip(nameTuple,workTuple))
print("zippedList = ",zippedList)
