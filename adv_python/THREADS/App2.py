import threading
''' Thread(target,args) -> Thread object '''

class Demo:
    def method1(self):
        for i in range(1,11):
            print("Mtd-1 of Demo ...",i)

    def method2(self):
        for i in range(30,41):
            print("Mtd-2 of Demo ... ",i)

#calling
d=Demo()
t1=threading.Thread(target=d.method1)
t2=threading.Thread(target=d.method2)
t1.start()
t2.start()
