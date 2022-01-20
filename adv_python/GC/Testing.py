import time

class Sample:
    def __init__(self):
        time.sleep(1)
        print("Constructor is Invoked ")    
        print("- "*30)

    def __del__(self):
        time.sleep(1)
        print("Dest is invoked ")        

#calling
s1=Sample()
s2=s1
s3=s2

s3=None
s2=None
s1=None
