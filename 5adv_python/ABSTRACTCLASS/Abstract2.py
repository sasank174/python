
from abc import ABC,abstractmethod
class Super(ABC):
    def method1(self):   #non abstract mtd
        print("Mtd-1  of Super ")

    @abstractmethod
    def method2(self):
        pass

class Sub(Super):
    pass

#calling
s=Sub()
    
