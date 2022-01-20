import time

class Super:
    @classmethod
    def method1(cls):
        time.sleep(1)
        print("Cls mtd-1 of Super ")

    @staticmethod
    def method2():
        time.sleep(1)
        print("Static mtd-2 of Super ")

class Sub(Super):
    def method3(self):
        self.method1()
        Super.method1()
        print("- "*30)
        self.method2()
        Super.method2()
        print("- "*30)
        Sub.method1()
        Sub.method2()
        print("- "*30)
        print("Instance mtd-3 of Sub")

#calling
s=Sub()
s.method3()
print("From Outside Of Classes")
s.method1()
s.method2()



