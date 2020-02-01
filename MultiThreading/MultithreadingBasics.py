from threading import Thread

print("For Thread we need to extends our class from Thread Class, And that class is apart of threading class")
print("For creating thread we need to use start() method , and provide our body in class using run() method")

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")

t1 = Hello()
t2 = Hi()
print("\nif we call run method directly then it act as a normal method :")

t1.run()
t2.run()

print("\nif we call run method directly then it act as a normal method :")

print("\nif we create thread then we need to call start() method :")

t1.start()
t2.start()

print("\nif we create thread then we need to call start() method :")
