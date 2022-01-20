class Super:
    def method1(self):
        print("Instance mtd-1 of Super ")

    @classmethod
    def method2(cls):
        print("Cls mtd-2 of Super")
        print(" - "*30)

    @staticmethod
    def method3():
        print("Static mtd-3 of Super ")
        print(" - "*30)

class Sub(Super):
    pass

#calling
s=Sub()
s.method1()
s.method2()
Sub.method2()
s.method3()
Sub.method3()
