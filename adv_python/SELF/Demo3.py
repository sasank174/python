import time
class Sample:
    def method1(self):
        print("Mtd-1 of Sample")
        print(self)

    def method2(x,y,z):
        print("Mtd-2 of Sample")
        print("self : ",x)
        print("y : ",y)
        print("z : ",z)

#calling
s=Sample()
s.method1()
time.sleep(3)
s.method2(30,40)
        
