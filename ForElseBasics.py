print('We can use for else when we use break, if break not execute then we will get for associated else data.')

x = [10,20,11,13]
for i in x:
    if i % 5 == 0:
        print(i)

print('Bye')

for i in x:
    if i % 5 == 0:
        print(i)
        break

print('Bye')

x = [12,16,18]
for i in x:
    if i % 5 == 0:
        print(i)
        break
else:
    print("Not found ")

print('Bye')
