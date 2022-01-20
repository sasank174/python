import time

class Super:
    x=111 #static variable
    def method1(self):
        self.y=222

class Sub:
    def method2(self):
        print("Instance mtd-2 of Sub")
        print("static x from super_class : ",Super.x)
        su=Super()
        print("static x from super_class : ",su.x)
        su.method1()
        print("Instance y from super_class : ",su.y)

#calling
s=Sub()
s.method2()
        
    
