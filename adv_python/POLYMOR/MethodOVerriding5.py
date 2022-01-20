''' super(Classname,currentclassobject).methodname([list of args]) '''

class A:
    def method(self):
        print("Mtd-A")

class B(A):
    def method(self):        
        print("Mtd-B")

class C(B):
    def method(self):
        super(B,self).method()
        print("Mtd-C")

#calling
c=C()
c.method()
