def func():
    print("sasank")
func()

def func(s,a="hee"):
    print(a,s)
func("sasank","hai")


def my_function(*kids):
  print("The youngest child is " + kids[2])
  print(type(kids))

my_function("Emil", "Tobias", "Linus")

def my_function(**kids):
  print("The youngest child is " + kids["s"])
  print(type(kids))

my_function(s = "Emil", a = "Tobias", b ="Linus")


def func(s):
    return s*2
print(func("sasank"))