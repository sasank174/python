
''' if we define sub class constructor same as super class constructor
   then priority is given to sub class constructor

   if u want call the super class constructor by sub class constructor
           then we have to use  super().__init__([parameters])   '''

class Super:
    def __init__(self):
        print("Def constructor of Super ")

class Sub(Super):
    def __init__(self):
        super().__init__()
        print("Def Constructor of Sub ")

#calling
s=Sub()
