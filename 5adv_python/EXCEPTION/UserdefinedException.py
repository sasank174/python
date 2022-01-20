''' raise ExceptionClsName([list of args]) '''

class MyLoginError(Exception):
    def __init__(self,msg):
        self.msg=msg

#main_logic
username=input("Enter username ")
password=input("Enter password ")

if username=="sssit" and password=="kphb":
    print("Valid User  ....!!! ")
else:
    try:
        raise MyLoginError("Invalid UN or PW ...")
    except MyLoginError as r:
        print("Sorry Unable to continue ....")
        print("Reason is : ",r)
    
