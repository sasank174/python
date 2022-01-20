class Student:
    def setStudent(self):
        self.no=input("Enter sno : ")
        self.name=input("Enter sname : ")
        self.d=self.Dob()
        self.d.setDob()
        self.m=self.Marks()
        self.m.setMarks()

    def getStudent(self):
        print("\n\n ")
        print("Sno is : ",self.no)
        print("Sname is : ",self.name)
        self.d.getDob()
        self.m.getMarks()       
        
    class Dob:
        def setDob(self):
            print("Enter DOB ")
            self.dd=input("Enter DD : ")
            self.mm=input("Enter MM : ")
            self.yy=input("Enter YY : ")

        def getDob(self):
            print("Dob is {}-{}-{}".format(self.dd,self.mm,self.yy))

    class Marks:
        def setMarks(self):
            self.m1=int(input("Enter m1 : "))
            self.m2=int(input("Enter m2 : "))
            self.m3=int(input("Enter m3 : "))            

        def getMarks(self):
            print("M1 : ",self.m1)
            print("M2 : ",self.m2)
            print("M3 : ",self.m3)
            print("= "*30)
            print("Total is : ",self.m1+self.m2+self.m3)

#calling
s=Student()
s.setStudent()
print("- "*30)
s.getStudent()














