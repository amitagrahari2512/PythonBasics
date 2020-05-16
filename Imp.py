a = 'good'
print (a + a[::-1])
print (a + a[:-1])
print (a + a[0:3])

print("----------------------------------------------")
a = 15/3;
print(a)
a = 15//3;
print(a)

print("----------------------------------------------")

print("Divmod")
print(divmod(10.5,5))
print(divmod(2.4,1.2))
print(divmod(10,5))
print(divmod(24,12))

print("----------------------------------------------")

a = [1,2,3]
b = list(a)
if all((a==b, a is b)):
    a.append(b)
else:
    a.extend(b)

print(a)


print("----------------------------------------------")

a = tuple('abcde')
print(a)
a, b, c, d, e = a
b = c = '*'
a = (a, b, c, d, e)
print(a)

print("----------------------------------------------")

m = [1,2,3,4,5]
print(m[1:])
print(m[:1])
d = lambda y : (d (y [1 :]) + y [:1] if y else [])
print(d(m))

print("----------------------------------------------")

a = list(map(lambda x : x**2,range(10)))

b = {x**2 for x in range(10)}

print(a)
print("type(a)",type(a))
print(b)
print("type(b)",type(b))

print("a==b :",a==b)
print("a is not b :",a is not b)
print("type(a) == type(b) :",type(a) == type(b))


print("----------------------------------------------")

b = set([3,5,7,9])
print(b)

c = set((3,5,7,9))
print(c)

d = {3,5,7,9}
print(d)

print("Error while Calling")
print(" a = set([[3,5],[7,9]]) \n print(a)")


print("----------------------------------------------")
import copy

values = [1, {'a' : 2}]

values2 = copy.copy(values)
values2[1]['b'] = 3
values2[0] = 42

values3 = copy.copy(values)
values3[1]['c'] = 4

print(values)


print("----------------------------------------------")

i =1
s = "A"
k = int(s,16)
print("k : ",k)
while True:
    if i%k == 0:
        break
        print(i,end =',')
        i += 1
