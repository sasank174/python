'''
  1. object is the super class for every class in python
  2. if any class inherited with other class then the current class
      is the indirect sub_class of object
  3. if any class not inherited with other class then the current
      class is the direct sub class of object.'''


class A:
    pass

class B(A):
    pass

class C(object):
    pass

print("A is the sub class of object ? : ",issubclass(A,object) ) #True
print("B is the sub class of object ? : ",issubclass(B,object) ) #True
print("C is the sub class of object ? : ",issubclass(C,object) ) #True

print("B is the sub class of A ? : ",issubclass(B,A) )#True
print("A is the sub class of B ? : ",issubclass(A,B)) #False







