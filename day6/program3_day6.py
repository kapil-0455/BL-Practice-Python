

# 3.1  Counting Letters, Digits, and Special Symbols in a String Using Explicit Loops
'''
def print_counting_of_characters(string):
    alpha_count =0
    digit_count = 0
    special_char_count = 0

    for ch in string:
        if(ch.isalpha()):
            alpha_count +=1 
        elif (ch.isdigit()):
            digit_count +=1
        else :
            special_char_count += 1


    print(f"Alphabets in given String : {alpha_count}")
    print(f"Digit in given String : {digit_count}")
    print(f"Special characters in given String : {special_char_count}")

def main():
    string = input('Enter your String : ')
    print_counting_of_characters(string)


if __name__ == "__main__":
    main()
'''


#3.2 Counting Letters, Digits, and Special Symbols in a String Using List Comprehension
def print_counting_of_characters(string):
    alpha_count = sum(1 for ch in string if ch.isalpha())
    digit_count = sum(1 for ch in string if ch.isdigit())
    special_char_count = sum(1 for ch in string if not ch.isalpha() and not ch.isdigit())

    print(f"Alphabets in given String : {alpha_count}")
    print(f"Digit in given String : {digit_count}")
    print(f"Special characters in given String : {special_char_count}")

def main():
    string = input('Enter your String : ')
    print_counting_of_characters(string)


if __name__ == "__main__":
    main()
