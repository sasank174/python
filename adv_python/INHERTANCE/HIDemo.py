class Person:
    def setPerson(self):
        self.no=input("Enter no :")
        self.name=input("Enter name : ")

    def getPerson(self):
        print("no is : ",self.no)
        print("name is : ",self.name)

class Student(Person):
    def setStudent(self):
        self.setPerson()
        self.course=input("Enter Course : ")

    def getStudent(self):
        self.getPerson()
        print("Course is : ",self.course)

class Employee(Person):
    def setEmployee(self):
        self.setPerson()
        self.job=input("Enter Job : ")

    def getEmployee(self):
        self.getPerson()
        print("Job is : ",self.job)

'''Calling '''
s=Student()
s.setStudent()
print("- "*30)
s.getStudent()
print("- "*30)

e=Employee()
e.setEmployee()
print("- "*30)
e.getEmployee()















    
    
