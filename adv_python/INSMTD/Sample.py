
class Sample:
    def setData(self):
        a=10 #local
        print("local a is : ",a)
        self.x=111
        self.y=222
        print(" - "*30)

    def getData(self):
        # print("a val is : ",a) #NameError
        print("x val is : ",self.x)
        print("y val is : ",self.y)

#calling
s=Sample()
s.setData()
s.getData()
