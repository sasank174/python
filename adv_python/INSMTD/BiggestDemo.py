
class Biggest:
    def setData(self,a,b):
       self.x=a
       self.y=b

    def findBiggest(self):
        if self.x>self.y:
            print("Biggest is : ",self.x)
        else:
            print("Biggest is : ",self.y)
            
#calling
b=Biggest()
b.setData(10,20)
b.findBiggest()
    
        
