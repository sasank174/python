

class Super:
    def method1(self):
        print("Mtd-1 of Super ")

class Sub(Super):
    def method1(self):
        super().method1()
        print("Mtd-1 of Sub ")

#Calling
s=Sub()
s.method1()
