
''' Data abstraction can be done in Python
     Using private | public [ two ]  | protected [not] ]

    > In Python there is no keyword "private "
    > private members are declared in python using ___variable
    > private members can be accessed only inside of the class
    > private members are not inherited |
    > can't be accessed outside of the class '''

class Super:
    def method1(self):
        print("Mtd-1 of Super")
        self.__x=10  #private
        print("private x val is : ",self.__x)
   
#calling
s=Super()
s.method1()
print("From Outside of the class ")
''' we can also access private members by using refvname._classname__privatefield '''
print("private x from Super ",s._Super__x)







        


     

     
