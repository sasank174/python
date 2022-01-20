
class Super:
    def method1(self):
        print("Instance mtd-1 of Super ")

class Sub(Super):
    pass

#calling
s=Sub()
s.method1()
