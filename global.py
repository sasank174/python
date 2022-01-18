x = "sasank"
print(x)

def func():
    x = "nice"
    print(x)

def func2():
    global x
    x = "nice"
    print(x)

func()
func2()
print(x)