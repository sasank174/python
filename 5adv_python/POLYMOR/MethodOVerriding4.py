
class A:
    def methodA(self):
        print("Mtd-A")

class B(A):
    def methodB(self):
        super().methodA()
        print("Mtd-B")

class C(B):
    def methodC(self):
        super().methodB()
        print("Mtd-C")

#calling
c=C()
c.methodC()
