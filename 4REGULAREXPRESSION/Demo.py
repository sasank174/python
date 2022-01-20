
# To Specify Pattern
#       compile(str) -> pattern

# To Specify the Target
#       match(str) -> Match | None
#         - To ensure the first word of the target is matched with pattern or not
        
#       search(str) -> Match | None
#          - To ensure any matches are existed in the target but it wll extract only the first

#       findall(str) -> list
#          - It will extract all the matches from target .
#          - if none of match then it will return an empty [ ]

#      finditer(pattern,target) -> callable_iterator
#             callable_iterable is  the collection of match objects

#      fullmatch(pattern,target) --> Match Object

#      sub()
#      subn()
#      split()
             

# To get the Details of Matched Patterns
#      start( ) -> int | to extract starting index pos of match
#      end( ) -> int | to extract ending index pos + 1 of match
#      group( ) -> str | to extract matched string
#           start() | end( ) and group( ) from Match class

# Predefined Patterns

# \w  ---> Any A|N value
# \W ---> Except A|N Value

# \d   --> Only digits
# \D  --> Except Digits

# \s --> Only Spaces
# \S --> Except  Spaces

# .  --> any thing

# ^ --> line Starts with
# $ --> Line Ends with  ....

# re.IGNORECASE

# Then We have to define Our Own Patterns Called Userdefined Patterns

# [a-z]   --> only lower case letters
# [A-Z] --> Only upper case letters

# [A-Za-z] --> only alpha
# [abc] --> Either a or b or c
# [a-c] --> from a to c

# [^a-z] --> Except lower case letters
# [^a-zA-Z] --> Except Alpha

# [a-zA-Z0-9] or \w    --> Any A|N
# [^a-zA-Z0-9] or \W  --> Except A\N

# Quantifier
#    "a" --> Only a
#    "a+" --> atleast one 'a' followed by n.no.of 'a's
#    "a?" -->   atmost one 'a' ie either 1'a or 0's will be cosidered as match
#    "a*" -->  0'a or any no.of. a's considered as match

# Example Pattern For Validate Mobile number :
#    -> it must have to 10 digits
#    -> It need to starts with 6 |7 | 8 | 9

# [6789][0-9][0-9][0-9]
# 		    [0-9][0-9][0-9]
# 			[0-9][0-9][0-9]

# [6-9][0-9]+   // Wrong Pattern
#   76 
#   768
#   7689
#   789494506984569804985609485609406

# [6-9][0-9]*  // Wrong Pattern
#   9
#   989898
#   989889988888888888

# [6-9][0-9]{9}  //100% correct
# ================================================
# Example 2:
# Pattern For Mobile number 
#     -> it must be start with 6|7|8|9
# 	-> it may have 10digits or 11 digits
# 	-> If it is 11 digit then it will starts with 0

# [6-9][0-9]{9} ---> 10 digits
# 0[6-9][0-9]{9} --> 11 digits

# 0?[6-9][0-9]{9} --> 110% valid 

# Example 2:
# Pattern For Mobile number 
# 	-> it must be start with 6|7|8|9
# 	-> it may have 10digits or 11 or 12 digits
# 	-> If it is 11 digit then it will starts with 0
# 	-> If it is 12 digit then it will starts 91

# 	91?0?[6-9][0-9]{9}   //Wrong Patter
#     91069848022338

#     (91|0)?[6-9][0-9]{9}    //100% correct
# 	9169848022338
#                   069848022338

#                   ==================================================
# Pattern For Mail-Id only gmail
# 1|----------------------2-------|@ |------3------|
# s hashikumar.chukkala @ gmail.com
# [a-zA-Z0-9][a-zA-Z0-9._]+@gmail[.]com

# Pattern Form Any Mail-Id
#                                                  gmail.com
# 												 yahoo.com
# 												 tv9.com
# 												 eenadu.net

# [a-zA-Z0-9][a-zA-Z0-9._]+@[a-z0-9]+[.][a-z]+
# =====================================================
#                                                  gmail.com
#                                                  yahoo.edu
#                                                  tv9.in
#                                                  us.edu.in
#                                                  uk.eenadu.net
#                                                  ts.ind.gov.co

# [a-zA-Z0-9][a-zA-Z0-9_.]+@[a-z0-9]+ [ [.][a-z]+ ]+







                  
