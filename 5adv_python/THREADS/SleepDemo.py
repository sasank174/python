import threading
import time

def task1():
    print("Take a bowl and milk")
    print("Put in on the flame for 5 min...")

def task2():
    print("Add Tea powder ")
    print("Boil it for 3 min .... ")

def task3():
    print("Add Sugar ")
    print("Boil it for 2 min ....")
    print("Tea is Ready....!!! :)  ")

#__main__
t1=threading.Thread(target=task1)
t2=threading.Thread(target=task2)
t3=threading.Thread(target=task3)
t1.start()
time.sleep(5)
t2.start()
time.sleep(3)
t3.start()
