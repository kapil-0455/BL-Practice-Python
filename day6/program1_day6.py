#A string is a sequence of characters.
# it is immutable
# it can declare in 3 types 

'''
# single Quotes - ''
# double Quotes = ""
# Triple Quotes = ''' ''' -> used for multilines 

eg ->
x = "multiline String" \
	"I love Python" \
	"Python Langauge"

in this \ backslash make them in single line
print(x)
'''


# basic functions 
'''
is_alpha() (referred to as is alpha)1 -> check it all alphabets  
is_digit() (referred to as is digit)2 -> check all charcters are digit 
is_alnum() -> check both digit or number 
upper() -> make them uppercase
lower()-> make them lower case
title() -> make every character first letter uppercase 
count() -> count frequnecy of any character 
replace()-> replace a word and a slice of string 
'''


# program 1 use joins

def print_names(num):
    city_names = []

    for i in  range(1 , num+1):
        city = input(f'Enter the name of place {i} : ')
        city_names.append(city)

    print(f'Places stored in list : {city_names}')
    places_str = ', '.join(city_names) # join then by comma and space and whatever you want
    print(f'All places separated by comma and space and in uppercase : {places_str}')


print_names(2)