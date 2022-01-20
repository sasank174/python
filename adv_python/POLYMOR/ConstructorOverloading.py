
class Sample:
    def __init__(self):
        print("0-parameterized Constructor ")

    def __init__(self,x):
        print("1-Parameterized Constructor ",x)

#calling
s=Sample(10)
s1=Sample(123)
