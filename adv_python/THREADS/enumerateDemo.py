
import time
import threading

def function():
    print("Thread ",threading.current_thread().getName()," started exectuion")
    time.sleep(5)
    print("Thread ",threading.current_thread().getName()," Ended execution ")

t1=threading.Thread(target=function,name="Ramesh")
t2=threading.Thread(target=function,name="Suresh")
t1.start()
t2.start()
lst=threading.enumerate()  #lst is the collection of active threads

for t in lst:
    time.sleep(1)
    print("Thread Name is : ",t.getName())
    print("Ident Of Thread : ",t.ident)
    print("- "*30)


