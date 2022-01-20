
import time
import threading

def child():
    print("Child Thread Waiting For Main Thread Execution ")
    mt.join()

#default thread is main_thread
mt=threading.currentThread()
t1=threading.Thread(target=child)
t1.start()
print("Main Thread is Waiting for Child Thread Execution")
t1.join()





