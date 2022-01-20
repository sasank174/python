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
        self.marks=[int(i) for i in input("Enter 3 sub marks with space").split()]
        
    def getMarks(self):
        i=1
        for m in self.marks:
            print("Sub_{} : {}".format(i,m))
            i=i+1
            
        print("- "*30)

class Student(Marks):
    def setStudent(self):
        self.setPerson()
        self.setMarks()
    
    def getTotal(self):        
        print("Total is : ",sum(self.marks))

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












        
