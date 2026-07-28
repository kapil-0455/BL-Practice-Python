# PROG 4: Count Character In The String
def count_characters(string):
    string = string.lower()
    counts = {}

    for ch in string:
        if ch.isalnum():   
            if ch in counts:
                counts[ch] += 1
            else:
                counts[ch] = 1

    return counts



string = input("Input String: ")
result = count_characters(string)
print("Character Counts:", result)