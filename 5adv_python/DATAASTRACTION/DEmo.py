
''' Data abstraction can be done in Python
     Using private | public [ two ]  | protected [not] ]

    > In Python there is no keyword "private "
    > private members are declared in python using ___variable
    > private members can be accessed only inside of the class
    > private members are not inherited | can't be accessed outside of the class '''

class Super:
    def method1(self):
        self.__x=10  #private

    def method2(self):
        print("Mtd-2 of Super ")
        print("x val is : ",self.__x)

#calling
s=Super()
s.method1()
s.method2()






        


     

     
