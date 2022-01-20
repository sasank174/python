class Sample:
    def method1(self):
        self.x=100

    def method2(self):
      print(self.x)

#calling
s=Sample()
s.method1()
s.method2()  #100
s.x=999
s.method2()#999
