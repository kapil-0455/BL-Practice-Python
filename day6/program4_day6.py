
# Regex (Regular Expressions) is a sequence of characters that defines a search pattern
'''
Most Common Functions in re

re.match() ->	Matches only at the beginning of the string
re.search()->	Searches anywhere in the string
re.findall()->	Returns all matches as a list
re.finditer()->	Returns an iterator of match objects
re.sub()	->  Replaces matched text
re.split()	->  Splits a string using a regex pattern
re.fullmatch() ->Entire string must match
'''

#<------------------------------------------------------------------>
'''
\d
- Meaning: Matches any digit
- Range: 0 to 9
- Example Matches: 0, 5, 9

eg:
text = "Age is 25"
print(re.findall(r"\d+", text)) # serach all digit once or more 

# search starting first 4 matches group by group
print(re.findall(r"\d{4}", text))


Output:
['2', '5']
'''

#<------------------------------------------------------------------>

'''
\D
- Meaning: Matches any character that is NOT a digit
- Example Matches: a, A, #, $

eg:
text = "Age is 25"

# do search for non digit 
print(re.findall(r"\D+", text)) # ['A', 'g', 'e', ' ', 'i', 's', ' ']
print(re.findall(r"\D{4}", text))

'''

#<------------------------------------------------------------------>

'''
\w
- Meaning: Matches any word character
- Includes:
    - A-Z
    - a-z
    - 0-9
    - _ (underscore)
- Example Matches: abc123_

eg:
text = "Python_123!"
print(re.findall(r"\w", text)) # ['P', 'y', 't', 'h', 'o', 'n', '_', '1', '2', '3']
print(re.findall(r"\w{4}", text))


'''
#<------------------------------------------------------------------>

'''
\W
- Meaning: Matches any character that is NOT a word character
- Example Matches: @, #, %, !, space

eg -:

text = "Python_123!"
print(re.findall(r"\W", text))  # ['!']
print(re.findall(r"\W{3}", text))


'''

#<------------------------------------------------------------------>
'''
\s
- Meaning: Matches any whitespace character
- Includes:
    - Space
    - Tab (\t)
    - Newline (\n)
- Example Matches: ' ', '\t', '\n'

eg -:

text = "Hello World"
print(re.findall(r"\s", text)) # [' ']
print(re.findall(r"\s{3}", text))

'''

#<------------------------------------------------------------------>

'''
\S
- Meaning: Matches any character that is NOT a whitespace character
- Example Matches: a, 1, @, A

eg :-
text = "Hello World" # ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']
print(re.findall(r"\S", text))
print(re.findall(r"\S{3}", text))


'''

'''
\b used to check word where it start and where it end 
\bword\b -> 
'''

#Program 4 find all digits in string using regex
import re

def regex_digit_find(string):
    pattern = r'\d'
    digits = re.findall(pattern , string)

    return digits


string = input('Enter a String : ')
digit_found = regex_digit_find(string)

if digit_found:
    print(f'Digits found in a string : {digit_found}')
else:
    print('Digit not found ')


