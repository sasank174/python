
class Sample:
    x=10  #static variable
    def method1(self):
        x=20 #local variable
        self.x=30  #instance field
        print("Mtd-1 of Sample ")
        print("local x val is : ",x)
        print("Instance x val is : ",self.x)
        print("Static x val is : ",Sample.x)

#calling
s=Sample()
s.method1()
