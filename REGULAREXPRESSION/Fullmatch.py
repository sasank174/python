
''' fullmatch() returns match Object if total target is matched with
    given pattern else it will return None '''

import re
import time

number=input("Enter u r mobile number ")

match=re.fullmatch("0?[6-9][0-9]{9}",number)

if match is not None:
    print("Given number is valid number ")
else:
    print("Given number is invalid number")

