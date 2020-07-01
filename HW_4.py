# Enter a string of words separated by spaces. Find the longest word.
# string_of_words = input("Please, enter string: ")


def longest_word():
    string_of_words = input("Please, enter string: ")
    longest = ""
    for words in string_of_words.split():
        if len(longest) < len(words):
            longest = words
    return longest


print(longest_word())


# Enter an irregular string (that means it may have space at the beginning of a string, at the end of the string, and
# words may be separated by several spaces). Make the string regular (delete all spaces at the beginning and end of
# the string, leave one space separating words).

def irregular_string():
    string_of_words = input("Please, enter irregular string: ")
    return ' '.join((string_of_words.split()))


print(irregular_string())
