
class Student:
    def setStudent(self): #no,name,tot are local to setStudent  '''
        self.sno=input("Enter sno : ")
        self.sname=input("Enter sname : ")
        self.stot=input("Enter stot : ")

    def getStudent(self):
        print("Sno is : ",self.sno)
        print("Sname is : ",self.sname)
        print("Stot is : ",self.stot)
        print("- "*30)

    def getTotal(self):
        return self.stot

#calling
s1=Student( )
s1.setStudent()

s2=Student()
s2.setStudent()

if s1.getTotal()>s2.getTotal():
    s1.getStudent()
else:
    s2.getStudent()





    
        
