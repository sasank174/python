import time
class Sample:
    z=333  #static variable
    
    @classmethod
    def method1(cls):
        print("class mtd-1 of Sample")
        print(cls)
        x=111 #local variable    
        print(" - "*30)
        print("Local x is : ",x)        
        print("static z is : ",Sample.z)

    
#calling
s=Sample()
s.method1()
