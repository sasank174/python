
class Sample:
    def method1(self):
        self.x=111
        self.y=222

    def method2(self):
        self.x=999
        self.y=888
        print("x val is : ",self.x)
        print("y val is : ",self.y)

#calling
s=Sample()
s.method1()
s.method2()
