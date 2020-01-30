print("For custom Iterator we need to use iter and __next__ in our custom class code")

class TopValues:
    def __init__(self,size):
        self.num = 1
        self.size = size

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= self.size:
            val = self.num
            self.num+=1
            return val
        else :
            raise StopIteration

values = TopValues(10)

print(values.__next__())
print(next(values))

for i in values: # for loop automatically catch exception
    print(i)