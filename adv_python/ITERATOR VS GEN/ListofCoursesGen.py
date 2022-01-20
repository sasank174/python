import time

def myCourse():
    yield "Android"
    yield "Python"
    yield "Django"

m=myCourse()
print("Type is : ",type(m))
print("m val is : ",m)

for i in m:
    time.sleep(1)
    print(i)
