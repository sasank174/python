

class Sample:
    @classmethod
    def  method1(cls):
        print("cls mtd-1 of Sample ")
        print("- "*30)

    def method2(self):
        self.method1()
        print("Ins mtd-2 of Samle ")

#calling
s=Sample()
s.method1()
Sample.method1()

s.method2()
