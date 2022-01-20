
import threading

def myFun():
    for i in range(1,11):
        print("MyFun Executed By ....",
              threading.current_thread().getName())

#__main__
t1=threading.Thread(target=myFun,name="Shashi")
t2=threading.Thread(target=myFun,name="Kumar")
t1.start()
t2.start()


