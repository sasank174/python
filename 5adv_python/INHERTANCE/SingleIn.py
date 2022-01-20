
class Person:
    def setPerson(self):
        self.no=input("Enter no : ")
        self.name=input("Enter name : ")

    def getPerson(self):
        print("No is : ",self.no)
        print("Name is : ",self.name)

class Student(Person):
    def setStudent(self):
        self.setPerson()
        self.course=input("Enter course : ")

    def getStudent(self):
        self.getPerson()
        print("Course is : ",self.course)

#calling
s=Student()
s.setStudent()
print("- "*30)
s.getStudent()
