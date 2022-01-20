import time
class Sample:
    def __init__(self):
        self.x=11
        self.y=22

    def getData(self):
        print("x val is : ",self.x)
        print("y val is : ",self.y)

#Calling
s1=Sample()
print("Data From s1")
s1.getData( )
s1=None

time.sleep(5)
s2=Sample()
print("Data From s2")
s2.getData()

time.sleep(3)
print("Data From s1")
s1.getData()
