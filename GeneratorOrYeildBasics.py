print("Generator is same like a iterator,"
      "but when we create iterator we need to provide __iter__() and __next__() function values"
      "but for generator iterator concept already provided by python , we need to use only yield(value) method"
      "It will automatically genarated the iterator with provide value")
print("When we use yield , we need not to use return, its automatically take care for return value.")
print("\n")

class GenTest:
    def values(self):
        yield 1
        yield 2

gen = GenTest()
values = gen.values()
print(values.__next__())
print(values.__next__())

print("\nNow here we create provide n no of squares generators : ")
class SquareGenerators:
    def __init__(self, num):
        self.num = num

    def squareGenerator(self):
        n = 1
        while n<=self.num:
            sq = n * n
            yield sq
            n +=1

sq = SquareGenerators(10)
sqFun = sq.squareGenerator()
for i in sqFun:
    print(i)
