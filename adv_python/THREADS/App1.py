
''' creating thread by using an already defined functions '''

import threading

def fun1():
    for i in range(1,11):
        print("Fun1 .... ",i)

def fun2():
    for i in range(20,31):
        print("Fun2 .... ",i)

#calling
t1=threading.Thread(target=fun1)
t2=threading.Thread(target=fun2)
t1.start()
t2.start()

'''note : if u want define any functions as thread then we have to use
         Thread(target=name of the function,args=parameter if req for that fun)
          --> Thread object  from threading module

    if u want execute the threads then we have to use start() from Thread Class'''



