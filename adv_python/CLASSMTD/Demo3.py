import time
class Sample:
    def method1(self):
        print("Instance mtd-1 of Sample")
        print(self)
        print(" - "*30)

    @classmethod
    def method2(cls):
        print("Mtd-2 of Sample ")
        print(cls)
        print("- "*30)

#calling
s=Sample()
s.method1()
time.sleep(3)
s.method2()
