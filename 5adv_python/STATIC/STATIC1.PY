
class Sample:
    x=10  #static variable

#calling
print("From Outside of the class ")
print("static x variable of Sample : ",Sample.x)

s=Sample()
print("static x variable of Sample : ",s.x)
