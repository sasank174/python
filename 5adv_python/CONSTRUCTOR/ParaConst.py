
class Circle:
    def __init__(self,rad): #rad is local variable
        self.rad=rad    #self.rad is an instance thus it can be access t.class

    def findArea(self):
        area=3.14*self.rad*self.rad
        return area


#calling
r=int(input("Enter Radius " ))
c=Circle(r)
ac=c.findArea()
print("Area of Circle is : ",ac)
