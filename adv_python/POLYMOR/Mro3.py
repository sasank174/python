
class A:
    pass

class B:
    pass

class C(A,B):
    pass

#calling
c=C()
lst=C.mro()

import time
for i in lst:
    time.sleep(1)
    print(i)

