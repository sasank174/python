
class Employee:
    def __init__(self):
        self.name=input("Enter name ")
        self.job=input("Enter job ")
        self.salpd=int(input("Enter salary per day ...? : "))

    def __mul__(self,other):
        return self.salpd*other.nwd        

class TimeSheet:
    def __init__(self):
        self.nwd=int(input("Enter No.of.Working Day ? : "))

    def __mul__(self,other):
        return self.nwd*other.salpd        

#calling
e=Employee()
t=TimeSheet()
ns=e*t   #  t.__mul__(e)
print("Netsalary is : ",ns)                    
