import threading
import time

def myFun1():
    print("MyFun1 : ",threading.current_thread().getName()," started Execution")
    time.sleep(3)
    print("MyFun1 : ",threading.current_thread().getName()," Ended Exeuction ")

#Calling
t1=threading.Thread(target=myFun1,name="Cat")
t2=threading.Thread(target=myFun1,name="Rat")
t1.start()
t2.start()
print("t1 isalive ? : ",t1.is_alive()) # Python 3.8 is_alive()    in python 3.7 isAlive()
print("t2 isalive ? : ",t2.is_alive())
print("Count of Active Thread : ",threading.active_count())

time.sleep(5)
print("- "*30)
print("t1 isalive ? : ",t1.is_alive())
print("t2 isalive ? : ",t2.is_alive())
print("Count of Active Thread : ",threading.active_count())




