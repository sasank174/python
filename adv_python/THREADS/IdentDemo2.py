
import time
import threading

def fun1():
    time.sleep(1)
    print("Fun1 ... : ")

def fun2():
    time.sleep(1)
    print("Fun2 ... : ")

t1=threading.Thread(target=fun1)
t2=threading.Thread(target=fun2)
t1.start()
t2.start()
print("Ident of Thread_1 : ",t1.ident)
print("Ident Of Thread_2 : ",t2.ident)
print("Default Thread is main Thread ")
cwt=threading.current_thread()
print("Ident of Main Thread : ",cwt.ident)



