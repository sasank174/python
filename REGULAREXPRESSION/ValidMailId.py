
import re

data=input("Enter U mail id :  ")           
match=re.fullmatch("[a-z0-9][a-zA-Z0-9._]+@[a-z0-9]+[.][a-z]+",data)

if match is not None:
    print("U r mail id is valid ")
else:
    print("Sorry Invalid Mail-Id")
