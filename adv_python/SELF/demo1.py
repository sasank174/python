import time

class Sample:
    def method1(self):
        print("Mtd-1 of Sample")
        print(self)

    def method2(self):
        print("Mtd-2 of Sample")
        print(self)

#calling
s=Sample()
print("From Outside of class ",s)
time.sleep(1)
s.method1()
time.sleep(1)
s.method2()
