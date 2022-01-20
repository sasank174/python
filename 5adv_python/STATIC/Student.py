import time
class Student:
    course="Java"
    def setStudent(self):
        self.sno=input("Enter sno ")
        self.sname=input("Enter sname ")

    def getStudent(self): #instance mtd
        print("Sno is : ",self.sno)
        print("Sname is : ",self.sname)
        print("Course is : ",self.course)

#calling
s1=Student()
s1.setStudent()
s2=Student()
s2.setStudent()

print("- "*30)
s1.getStudent()
s1.course="Django"

print("- "*30)
time.sleep(3)
s2.getStudent()
        
                     
