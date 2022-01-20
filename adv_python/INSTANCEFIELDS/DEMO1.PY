
class Sample:
    def method1(self):
        print("Mtd-1 of Sample ")
        x=10 #local variable
        self.y=20  #instance field
        print("x val is : ",x)
        print("y val is : ",self.y)        


#calling
s=Sample()
s.method1()
