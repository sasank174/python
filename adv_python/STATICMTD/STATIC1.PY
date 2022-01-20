class Sample:
    x=999 #static variable
    @staticmethod 
    def method():
        print("utility mtd of Sample ")
        print("static x is : ",Sample.x)

    @staticmethod
    def myAdd(x,y):
        print("Sum is : ",(x+y) )


#calling
Sample.method()
s=Sample()
s.method()
s.myAdd(10,20)
