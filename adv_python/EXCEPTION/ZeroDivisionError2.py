
x=int(input("Enter a number "))
y=int(input("Enter a number "))
try:
    z=x/y
except ZeroDivisionError:
    print("Sorry Values are not divided by Zero...!!!")
else:
    print("Result is : ",z)
