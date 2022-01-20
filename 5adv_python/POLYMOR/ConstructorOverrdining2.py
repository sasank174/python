
class Super:
    def __init__(self):
        print("Def constructor of Super ")

class Sub(Super):
    def __init__(self):
        print("Def Constructor of Sub ")

#calling
s=Sub()
