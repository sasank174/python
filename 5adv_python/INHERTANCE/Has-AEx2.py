import time
class Super:
    def method1(self):
        time.sleep(1)
        print("Instance mtd-1 of Super")

    @classmethod
    def method2(cls):
        time.sleep(1)
        print("cls mtd-2 of Super ")

    @staticmethod
    def method3():
        time.sleep(1)
        print("static mtd-3 of Super ")

class Sub:    
    def method4(self):
        su=Super()
        su.method1()
        su.method2()  # Super.method2()
        su.method3()  # Super.method3()
        
        print("instance mtd-4 of Sub")

#calling
s=Sub()
s.method4()
