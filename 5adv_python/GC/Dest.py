
import time

class Sample:
    def __init__(self):
        time.sleep(1)
        print("Constructor is Invoked ")
        print("Res Allocation is Done...!!! ")
        print("- "*30)

    def __del__(self):
        time.sleep(1)
        print("Dest is invoked ")
        print("Res DE-Allocation is Done....!!! ")

#calling
s1=Sample()
s2=Sample()
s3=Sample()

s1=None
s2=None
s3=None

