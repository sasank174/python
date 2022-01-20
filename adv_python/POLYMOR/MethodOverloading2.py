import time

class Sample:
    def sum(self,x=None,y=None,z=None):
        time.sleep(1)
        if x!=None and y!=None and z!=None:
            s=x+y+z
            print("Sum with 3 args ",s)
        elif x!=None and y!=None:
            s=x+y
            print("Sum with 2 args ",s)
        elif x!=None:
            print("Sum with 1 arg : ",x)
        else:
            print("Req min arg max 3 args....! ")           

#calling
s=Sample()
s.sum(10,20,30)
s.sum(30,40)
s.sum(50)
s.sum()
