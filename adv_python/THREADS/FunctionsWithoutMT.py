
import time

def fun_sq(x):
    for i in x:
        time.sleep(1)
        s=i*i
        print("SQ :::> ",s)

def fun_cu(x):
    for i in x:
        time.sleep(1)
        c=i*i*i
        print("CQ :::> ",c)

#calling
lst=list(range(1,11))
st=time.time()
fun_sq(lst)
fun_cu(lst)
et=time.time()
tt=et-st
print("Total Time Take :",tt)



