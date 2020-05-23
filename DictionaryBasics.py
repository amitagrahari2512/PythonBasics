print("maps or list")
d = {"Amit":"onePlus","Himanshu":"Moto","AmitB":"MI"}
print(d)
print("type : ", type(d))
print("keys in dictionary : ", d.keys())
print("values in dictionary ; ", d.values())
print("Get data from [key] : ",d["Amit"])
print("Get data from get(key) method : ", d.get("Amit"))

print("Irerate Dictionary")

for i in d:
    print("Key : ",i)

for i,j in d.items():
    print("Key : {}, value : {}".format(i,j))