
class Sample:
    def method1(self):
        print("Mtd-1 of Sample")
        x=10
        self.x=20
        print("local x val is : ",x)
        print("Instance x val is : ",self.x)
        print("- "*30)

    def method2(self):
        print("Mtd-2 of Sample")
        ''' print("x val is : ",x) #NameError '''
        print("Instance x val is : ",self.x)

#calling
s=Sample()
s.method1()
s.method2()
