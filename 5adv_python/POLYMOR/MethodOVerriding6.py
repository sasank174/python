''' super(Classname,currentclassobject).methodname([list of args]) '''

class A:
    def method(self):
        print("Mtd-A")

class B:
    def method(self):        
        print("Mtd-B")

class C(B,A):
    def method(self):
        super().method()
        print("Mtd-C")

#calling
c=C()
c.method()
