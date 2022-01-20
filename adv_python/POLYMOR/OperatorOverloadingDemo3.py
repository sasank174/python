
class Student:
    def __init__(self):
        self.sname=input("Enter name " )
        self.scity=input("Enter city  ")
        self.sage=int(input("Enter age "))

    def getData(self):
        print("Younger Student is : ")
        print("sname is : ",self.sname)
        print("scity is : ",self.scity)
        print("sage  is : ",self.sage)

    def __lt__(self,other):
        if self.sage<other.sage:
            return True
        else:
            return False        

#calling
s1=Student()
s2=Student()
if s1<s2:
    s1.getData()
else:
    s2.getData()
