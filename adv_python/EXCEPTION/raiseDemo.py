''' Syn: raise ExceptionClassName([list of args])  '''

age=int(input("Enter Age : "))

if age<18:
    try:
        raise ValueError()
    except ValueError:
        print("Sorry Invalid Age Group For Vote ")
else:
    print("Elig For Vote ")
