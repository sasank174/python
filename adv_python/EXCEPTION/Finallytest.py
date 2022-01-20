import time

try:
    time.sleep(1)
    print("try :")
    print(" 1 ")
    print(" 2 ")
    raise IndexError()
except ZeroDivisionError:
    time.sleep(1)
    print("except ")
    print(" 4 ")
    print(" 5 ")
else:
    time.sleep(1)
    print("else")
    print(" 6 ")
    print(" 7 ")
finally:
    time.sleep(1)
    print("finally ")
    print(" 8 ")
    print(" 9 ")

time.sleep(1)
print("From outside of finally")
print(" 10 ")
print(" 11 ")
print(" NT ")
    
