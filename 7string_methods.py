x = "hello i am sasank"

print(x.endswith("sasank.")) # if str ends with sasank.
print(x.startswith("sasank")) # if str start with sasank

print(x.isalnum()) # contains only alphabets or numbers or both
print(x.isalpha()) # contains only alphabets
print(x.isnumeric()) #contains only numbers

print(x.isidentifier()) # it can be variable or not

print(x.lower()) # lowers all letters
print(x.islower()) # all lower or not

print(x.upper()) # lowers all upper
print(x.isupper()) # all letters uppercase

print(x.title()) # make word to start with a uppercase
print(x.istitle()) # each word start with a uppercase


print(x.ljust(20,"o")," is my favorite fruit.") # bananaOOOOOOOOOOOOOO is my favorite fruit.
print(x.rjust(20,"o")," is my favorite fruit.") # OOOOOOOOOOOOOObanana is my favorite fruit.

print(x.capitalize()) # calptilise 1st letter of sentense
print(x.casefold()) # lowers all letters

print(x.center(50,"*")) # ****************hello i am sasank*****************
print(x.count("sasank")) # count of sasank in str
print(x.find("sasank")) #  first occurence index
print(x.index("sasank")) # first occurence index
print(x.replace("sasank","asasank")) # replace all words
print(x.rfind("sasank")) # last occurence index
print(x.rindex("sasank")) # last occurence index

print(x.partition("sasank")) # ('hello i am ', 'sasank', '')
print(x.rpartition("sasank")) # from right ('hello i am ', 'sasank', '')

print("#".join(x)) # joins with #
print(x.split(" ")) # splits with " "
print(x.splitlines()) # splits sentence where "\n"

print(x.swapcase()) # swaps case

print(x.zfill(20)) # fills 0's to make 20 len