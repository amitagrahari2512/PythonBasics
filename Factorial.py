def fact(n):
    f = 1
    for i in range(1,n+1):
        f = f*i
    return f

f = fact(5)
print(f)