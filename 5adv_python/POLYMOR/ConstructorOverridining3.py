import time

class Student:
    def __init__(self,**kwargs): #**kwargs acts as dict collection
        time.sleep(1)
        for k,d in kwargs.items():
            time.sleep(.2)
            print(k,d,sep='----->')
        print("= "*30)              

#calling
s1=Student(sno=101)
s2=Student(sno=102,sname="Ramesh")
s3=Student(sno=103,sname="Sudha",sage=34)

        
        
