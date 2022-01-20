

class Sample:
    def method1(self):
        print("Ins mtd-1 of Sample")

    def method2(self):
        self.method1()
        print("Ins mtd-2 of Sample")


#calling
s=Sample()
s.method2( )
