from threading import Thread
from time import  *

print("sleep(time) is a method which can wait thread as a time provided in it")
print("sleep(time) is in time class , so we need to import this class")

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

print("\nif we create thread then we need to call start() method :")
