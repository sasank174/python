import time

class Sample:
    def __init__(self):
        time.sleep(1)
        print("Constructor is Invoked ")    
        print("- "*30)

    def __del__(self):
        time.sleep(1)
        print("Dest is invoked ")        

#calling
lst=[Sample(), Sample( ), Sample()]
del lst
