print("Iterate List")
x = [2, 4, 'Amit']

for i in x:
    print(i)

print("Iterate String")
x = 'Amit'
for i in x:
    print(i)

print("Initialize List direct in for loop iteration")
for i in [2,4 , 'PPPP'] :
    print(i)

print("Initialize String direct in for loop iteration")
for i in 'Amit':
    print(i)

print("We can use range also in for loop")
print("range(endNo(exclusive))")
print("range(startNo,endNo(exclusive),gap)")
print("range(10)")
for i in range(10):
    print(i)


print("range(11,21,1)")
for i in range(11,21,1):
    print(i)

print("range(11,21,2)")
for i in range(11,21,2):
    print(i)

print("range(20,10,-1)")
for i in range(20,10,-1):
    print(i)
