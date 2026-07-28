def check_modi(news):
    return "modi" in news.lower()


def count_words(news):
    return len(news.split())


def count_the(news):
    words = news.lower().split()
    return words.count("the")


def check_digits(news):
    for ch in news:
        if ch.isdigit():
            return True
    return False


def remove_articles(news):
    words = news.split()
    new_words = [word for word in words if word.lower() not in ["a", "an", "the"]]
    return " ".join(new_words)


def remove_vowels(news):
    vowels = "aeiouAEIOU"
    words = news.split()

    new_words = []
    for word in words:
        new_word = "".join([ch for ch in word if ch not in vowels])
        new_words.append(new_word)

    return " ".join(new_words)



news_paragraph = input("Enter News Paragraph:\n")


print("Presence of 'Modi':", check_modi(news_paragraph))
print("Number of words:", count_words(news_paragraph))
print("Number of occurrences of 'the':", count_the(news_paragraph))
print("Presence of digits:", check_digits(news_paragraph))
print("Compact news data without articles:")
print(remove_articles(news_paragraph))
print("Compact news data without vowels:")
print(remove_vowels(news_paragraph))