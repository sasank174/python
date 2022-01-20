'''
  1. Class is the collection of non abstract methods
  2. Abstract class is the collection of both abstract or non abstract mtds
  3. Interface  is the collection of only abstract methods
              Interface is the pure abstract class

    Note: if we define any abstract class with only abstract methods then that
               abstract class is acts as an interface '''    " Exception Handling"
                                                                                                      O

from abc import ABC,abstractmethod
class Super(ABC):
    @abstractmethod
    def method1(self):
        pass

class Sub(Super):
    def method1(self):
        print("OR Mtd-1 pf Super")
        
#Calling
s=Sub()
s.method1()








   
