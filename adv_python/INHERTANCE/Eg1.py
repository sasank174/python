
class Super:
    def method1(self): #instance mtd
        print("instance mtd-1 of Super ")

class Sub:
    def method2(self):
        sp=Super()
        sp.method1()
        print("instance mtd-2 of sub")

#calling
s=Sub()
s.method2()    
