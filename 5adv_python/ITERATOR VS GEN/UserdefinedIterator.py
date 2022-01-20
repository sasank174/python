
''' str | list | tuple | set |dict ... '''
import time

class Course:
    def __init__(self):
        self.courses=["android","java","python","django","go-lang","DigitalM"]
        self.index=-1

    def __iter__(self):
        return self

    def __next__(self):
        self.index=self.index+1
        if self.index<len(self.courses):
            return self.courses[self.index]
        else:
            raise StopIteration()    
        

c=Course()

for i in c:
    time.sleep(.1)
    print(i)

''' Creating userdefined iterable object
     if u want define u r class as an iterable class then
    step-1 : we must override the following the methods
                  __iter__(self) and __next__(self)

    step-2: __iter__(self) must return current class object
                  __next__(self) should return next item '''

class Shashi:
    pass

s=Shashi()
for i in s:
    pass





