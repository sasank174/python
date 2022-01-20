import time

class Maths:
    def sum(self,*x):   # *x varargs parameter   varargs => tuple
        time.sleep(1)
        print("Elements : ",x)
        print("Sum is : ",sum(x))   # sum(iterable) -> sum
        print(" -  "*30)


#calling
m=Maths()
m.sum(40,30,40,50,60,70,20,40,60,70,80,90,30)
m.sum(10,20,30,40,50,60)
m.sum(10,20,30,40)
m.sum(10,20)
m.sum()
        
