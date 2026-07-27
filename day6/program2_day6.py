# String slicing 

# we can use postive indexing and negative indexing 
'''
name = 'Kapil' 
print(name[0])
print(name[-1]) # give last character and start form -1
'''

#slicing 
'''
s = 'hello world'

print(s[0:5])
print(s[0:])
print(s[:3])
print(s[0:6:2])
print(s[6:0:-1])
print(s[::-1])
'''

# program 2 Implement slicing


def implement_slice(string):
    start_ch = string[0]
    middle_idx = len(string) // 2
    end_ch = string[-1]

    new_string = start_ch + string[middle_idx] + end_ch

    print(new_string)


string = input('Enter a String : ')
implement_slice(string)





