''' raise ExceptionClsName([list of args]) '''

class AccountError(Exception):
    def __init__(self,msg):
        self.msg=msg

class Bank:
    def setAccount(self):
        self.acno=int( input("Enter acno : ") )

    def validate(self):
        if self.acno<0:
            try:
                raise AccountError("Invalid Account Number")
            except AccountError as a:
                print("Sorry Unable to Continue ")
                print("Reason : ",a)
        else:
            print("Valid Acno ")

#Calling
b=Bank()
b.setAccount()
b.validate()

    
