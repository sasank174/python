
class Sample:
    def method1(self):
        print("Mtd-1")
        x=10  #local variable
        self.y=20
        print("x val is : ",x)
        print("y val is : ",self.y)
        print("- "*30)
        

    def method2(self):
        print("Mtd-2")
        '''print(x)    NameError '''
        '''print(y)   NameError '''
        print("y val is : ",self.y) 

#calling
s=Sample()
s.method1()
s.method2()
print("From outside of the class ")
''' print("x val is : ",x) NameError '''
print("y val is : ",s.y)



