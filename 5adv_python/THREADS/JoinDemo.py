
import threading
import time

def fun1():
    for i in range(1,11):
        time.sleep(2)
        print("Fun1 ...",i)

def fun2():
    for i in range(20,31):
        print("Fun2 ... ",i)

t1=threading.Thread(target=fun1)
t2=threading.Thread(target=fun2)
t1.start()
time.sleep(10)
t2.start()
