class Sample:
    pass

#calling
s1=Sample()
s1.x=10
print("x val is : ",s1.x)

del s1.x
print("x val is : ",s1.x)  #AttributeError
