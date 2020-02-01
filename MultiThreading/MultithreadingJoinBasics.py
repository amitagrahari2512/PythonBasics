from threading import Thread
from time import  *

print("When we want tread needs to be join with main one , then after all statemnt is called in main thread"
      "so we need to use join()  method")

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

t1 = Hello()
t2 = Hi()

print("\nif we create thread then we need to call start() method :")

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()

print("\nif we create thread then we need to call start() method :")
