import time
class Remote:
    def __init__(self):
        self.channels=["Sports","news","songs","HBO"]
        self.index=-1

    def __iter__(self):
        return self

    def __next__(self):
        self.index=self.index+1
        if self.index<len(self.channels):
            return self.channels[self.index]
        else:
            raise StopIteration()            

#calling
r=Remote()
for i in r:
    time.sleep(.2)
    print(i)
