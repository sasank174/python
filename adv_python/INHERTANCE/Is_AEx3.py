import time

class Super:
    def method1(self):
        time.sleep(1)
        print("Instance mtd-1 of Super ")

class Sub(Super):
    def method2(self):
        self.method1()
        print("Instance mtd-2 of Sub")

#calling
s=Sub()
s.method2()
