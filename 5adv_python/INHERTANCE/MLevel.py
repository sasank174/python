import time

class Person:
    def setPerson(self):
        self.no=input("Enter no : ")
        self.name=input("Enter name : ")

    def getPerson(self):
        print("no is       : ",self.no)
        print("name is : ",self.name)
        print("- "*30)

class Marks(Person):
    def setMarks(self):
        self.m1=int( input("Enter m1 : ") )
        self.m2=int( input("Enter m2 : ") )
        self.m3=int( input("Enter m3 : ") )

    def getMarks(self):
        print("M1 : ",self.m1)
        print("M2 : ",self.m2)
        print("M2 : ",self.m3)
        print("- "*30)

class Student(Marks):
    def setStudent(self):
        self.setPerson()
        self.setMarks()
    
    def getTotal(self):
        self.tot=self.m1+self.m2+self.m3
        print("Total is : ",self.tot)

    def getStudent(self):
        self.getPerson()
        time.sleep(1)
        self.getMarks()
        time.sleep(1)
        self.getTotal()

'''Calling '''
s=Student()
s.setStudent()
s.getStudent()












        
