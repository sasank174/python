
import time

class Sample:
    def method1(self):
        print("Mtd-1 without argument ")

    def method1(self,x):
        print("Mtd-1 with 1 argument : ",x)

#calling
s=Sample()
s.method1(10)
s.method1( 123)
