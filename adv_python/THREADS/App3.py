
import threading

class cat(threading.Thread):
    def run(self):
        for i in range(1,11):
            print("Cat Thread ... : ",i)

class rat(threading.Thread):
    def run(self):
        for i in range(20,31):
            print("Rat Thread ))))))))>> : ",i)

#calling
c=cat()
r=rat()
''' c.run()
    r.run()  '''

c.start()
r.start()




    
