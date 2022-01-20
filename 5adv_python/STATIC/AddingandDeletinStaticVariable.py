class Sample:
    pass

#calling
Sample.x=111 #Adding a static variable to Sample Class
print("x val is : ",Sample.x) #111

s1=Sample()
s1.y=222  #Adding an instance field to s1 object
print("s1 y val is : ",s1.y)

s2=Sample()
s2.z=333 #adding an instance field to s2 object
print("s2 z val is : ",s2.z)

''' static variable can be referred by either classname or object referecne whenever u want
access it from outside of the class '''

print("static x from s1 : ",s1.x)
print("static x from s2 : ",s2.x)

print("- "*30)
s2.x=999  #adding an instance field with the name x inside of s2 object
print("s2 x : ",s2.x)  #999

del s2.x
print("s2 x : ",s2.x)
del Sample.x
print("s2 x : ",s2.x)













