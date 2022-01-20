import time
import threading
def fun_sq(x):
    for i in x:
        time.sleep(1)
        s=i*i
        print("SQ :::> ",s)

def fun_cu(x):
    for i in x:
        time.sleep(1)
        c=i*i*i
        print("CQ :::> ",c)

#calling
lst=list(range(1,11))
t1=threading.Thread(target=fun_sq,args=(lst,))
t2=threading.Thread(target=fun_cu,args=(lst,))
st=time.time()
t1.start()
t2.start()

t1.join()
t2.join()

et=time.time()
tt=et-st
print("Total time is taken by threads : ",tt)







