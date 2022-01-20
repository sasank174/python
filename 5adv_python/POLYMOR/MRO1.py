
class A:
    pass

#calling
a=A()
lst=A.mro()   # ['class A','class object']
print("MRO is ",lst)
