
''' Inorder to get Object of the current working thread then
   we have to use predefined  current_thread() -> Thread '''

import threading

cwt=threading.current_thread()
print("Current Working Thread :",cwt)
tname=cwt.getName()
print("Name of Thread is : ",tname)
print("- "*30)

print("Name of Thread is : ",threading.current_thread().getName())
threading.current_thread().setName("SssiT_Thread")
print("Name of Thread is : ",threading.current_thread().getName())
