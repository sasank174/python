import time

class Sample:
    def __init__(self,x=None,y=None,z=None):
        time.sleep(1)
        print("Cosntructor is Invoked ...With 0 | 1 | 2 | 3 Parameter")
    
#calling
s1=Sample(10,20,30)
s2=Sample(10,20)
s3=Sample(10)
s4=Sample()

