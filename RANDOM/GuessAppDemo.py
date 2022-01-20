
''' choice(iterable) -> item '''

import random,time

lst=["oracle","java","python","django","DS","DA"]
print("List : ",lst)

for i in range(1,11):
    time.sleep(1)
    item=input("Guess Any Word From above List ")
    ritem=random.choice(lst)
    if ritem==item:
        print("Yes !!! U R Guess Correct ")
        break
    else:
        print("Sorry Try again : )   ")
        
