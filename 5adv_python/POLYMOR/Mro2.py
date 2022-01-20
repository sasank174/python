
class A:
    pass

class B(A):
    pass

#calling
b=B()
lst=B.mro()   # [class B,class A,class object]
print("MRO is ",lst)
