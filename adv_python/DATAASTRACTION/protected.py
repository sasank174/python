
'''
  > protected keyword is not existed
  > in Python protected members are declared using _variable
  > protected members can used with in the class |
     protected members are inherited but protected members can't be accessed outside of cls'''

class Super:
    def __init__(self):
        self._x=10 #protected
        print("From Super protected x is : ",self._x)

class Sub(Super):
    def __init__(self):
        super().__init__()
        print("From Sub Protected x is : ",self._x)

#calling
s=Sub()
print("From outside of the class ")
print("Protected x val is : ",s._x)
