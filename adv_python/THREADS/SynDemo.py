
import threading,time

class ATM:
    def __init__(self):
        self.l=threading.Lock()
        
    def wd(self,name):
        self.l.acquire()
        for i in range(1,11):
            time.sleep(1)
            print("WD operation by Mr|Mrs. ",name)
        self.l.release()

#calling
a=ATM( )
t1=threading.Thread(target=a.wd,args=("Rames",) )
t2=threading.Thread(target=a.wd,args=("Suresh",) )
t1.start()
t2.start()
