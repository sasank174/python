
''' Default Thread in Python Main_Thread  and main thread
   is executed by PVM implicitly
   Thread(target,args) -> Thread object from threading module '''

import threading

def myFun():
    for i in range(1,11):
        print("MyFun ... : ",i)

#__main__
t1=threading.Thread(target=myFun)
t1.start()
for i in range(20,31):
    print("Main Thread ... : ",i)
