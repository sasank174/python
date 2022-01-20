
class Book_Python:
    def __init__(self):
        self.pages=100

    def __add__(self,other):
        #print("Self ClsName ",self.__class__)
        #print("Other ClsName ",other.__class__)
        s= self.pages + other.pages
        return s

class Book_Django:
    def __init__(self):
        self.pages=200

#calling
bp=Book_Python()
bd=Book_Django()
tp=bp+bd # '''    bp.__add__(bd) '''
print("Sum is : ",tp)

x=10
y=20
s=x+y
print("Sum is : ",s)

a="Shashi"
b="SssiT"
c=a+b
print("Result is : ",c) 
