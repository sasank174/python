import time
class Sample:
    z=333  #static variable
    def method1(self):
        print("Instance mtd-1 of Sample")
        print(self)
        x=111 #local variable
        self.y=222 #instance field
        print(" - "*30)
        print("Local x is : ",x)
        print("Instance y is : ",self.y)
        print("static z is : ",Sample.z)

    
#calling
s=Sample()
s.method1()
