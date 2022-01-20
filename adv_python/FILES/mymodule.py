#mymodule.py

class Employee:
    def setEmployee(self):
        self.eno=input("Enter eno : ")
        self.ename=input("Enter ename : ")
        self.esal=input("Enter esalary : ")

    def getEmployee(self):
        print("Eno is : ",self.eno)
        print("Ename is : ",self.ename)
        print("Esalary is : ",self.esal)
