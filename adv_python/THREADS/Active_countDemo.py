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
print("Count of Active Thread : ",threading.active_count())
time.sleep(5)
print("- "*30)
print("Count of Active Thread : ",threading.active_count())

