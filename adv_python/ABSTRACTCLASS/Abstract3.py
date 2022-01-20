
from abc import ABC,abstractmethod
class Super(ABC):
    def method1(self):   #non abstract mtd
        print("Mtd-1  of Super ")

    @abstractmethod
    def method2(self):
        pass

class Sub(Super):
    def method2(self):
        print("Override mtd-2 of Super")

#calling
s=Sub()
s.method1()
s.method2()
