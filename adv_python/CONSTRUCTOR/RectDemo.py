

class Rect:
    def __init__(self):
        self.l=4
        self.b=4

    def findArea(self):
        area=self.l*self.b
        return area

#calling
r=Rect()
ar=r.findArea()
print("Area of Rect : ",ar)
