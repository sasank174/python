
''' Whenever u define any thread by default every thread creating
   with their default names like Thread-1 | Thread-2 .....
   getName( ) -> str | name attribute of Thread class
   setName(str) -> None  '''   


import threading

def myFun():
    for i in range(1,11):
        print("MyFun ... : ",i)

#__main__
t1=threading.Thread(target=myFun)
tname=t1.getName()
print("Thread Name is : ",tname)
print("Thread Name is : ",t1.name)
print("- "*30)

#t1.setName("Child_Thread")
t1.name="Child_Thread2"
tname=t1.getName()
print("Thread NAme is : ",tname)











