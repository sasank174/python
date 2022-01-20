class Sample:
    def method1(self):
        self.x=111

#calling
s1=Sample()
s1.method1()
s2=Sample()
s2.method1()
print("Data From s1 ")
print("x val is : ",s1.x)

print("Data From s2")
print("x val is : ",s2.x)
print("- "*30)

s1.x=999
print("After modification ")
print("Data From s1")
print("x val is : ",s1.x)
print("Data From s2")
print("x val is : ",s2.x)

