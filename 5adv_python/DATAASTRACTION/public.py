
'''
   1.In Python there is not keyword "public"
   2.public member are without any __
   3.by default all members of the class is public
   4.public members can used in the class | inhertied classes |
      outside of class '''

class Super:
    def method1(self):
        self.x=10  #public
        print("Mtd-1 of Super ")
        print("x val is : ",self.x)
        
class Sub(Super):
    def method2(self):
        print("Mtd-2 of Sub")
        print("x val is : ",self.x)

#calling
sb=Sub()
sb.method1()
sb.method2()
print("From outside of the class ")
print("public x val is : ",sb.x)



        



        


        
   
