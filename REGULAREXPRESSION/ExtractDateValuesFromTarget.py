
''' fullmatch() returns match Object if total target is matched with
    given pattern else it will return None '''

''' dd-mmm-yyyy   \d{1,2}-[a-zA-Z0-9]{2,3}-\d{2,4} '''

import re
import time

data='''ramesh 12-jan-1987 sudha 2-DEC-1999 Roja 12-12-1998
    ramesh 12-09-87 sudha 2-11-1999 Roja 12-Mar-98 '''

lst=re.findall("\d{1,2}-[a-zA-Z0-9]{2,3}-\d{2,4}",data)

for i in lst:
    time.sleep(.5)
    print(i)
