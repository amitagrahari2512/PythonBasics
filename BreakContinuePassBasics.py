print('-------------------Break------------------')
available = 5
demand = 10

i = 1
while i < demand:
    if(i > available):
        print("out of stock")
        break

    print("candy")
    i += 1;

print("Bye")

print('---------------Continue----------')
for i in range (20):
    if(i % 2 != 0):
        continue
    print(i)

print('Bye')

print('----------------Pass--------------')
for i in range(20):
    if(i % 2 !=0 ):
        pass
    else:
        print(i)

print('bye')