# Write a Python function, which will count how many times a character (substring) is included in a string.
# DON’T USE METHOD COUNT
original_string = input("Please, enter string: ")
sub_string = input("Please, enter character (substring): ")


def count(string, character):
    if len(string) < len(character):
        return 0
    counter = 0
    while len(string) >= len(character):
        compare = string[:len(character):]
        if compare == character:
            counter += 1
        string = string[1::]

    return f'Character (substring) {sub_string} included {counter} times'


print(count(original_string, sub_string))


# Find and replace a substring in a string for another substring. User enter from a keyboard a string and
# both substrings. DON’T USE METHOD REPLACE
def replace():
    original = input("Please, enter string: ")
    substring = input("Please, enter string you need to replace: ")
    new_substring = input("Please, enter replace string: ")

    found = original.partition(substring)
    string_to_replace = str(found[1])

    while string_to_replace != '':
        original = str(found[0]) + new_substring + str(found[2])
        found = original.partition(substring)
        string_to_replace = str(found[1])
    return original


print(replace())


# Write a function for decompressing string “a4b3c2d”
string = "a4b3c2d"


def decompression(s):
    result = ""
    # count = 0
    for i in range(0, len(s), 2):
        if i < len(s) - 1:
            count = int(s[i + 1])
            while count >= 1:
                result += s[i]
                count -= 1
        else:
            result += s[i]
            return result


print(decompression(string))


# Recursion for Fib, factorial, digital root
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(7))


n = int(input('Input a number '))


def factorial(number):
    if number == 0:
        result = 1
    elif number > 0:
        result = number * factorial(number - 1)
    return result


print(factorial(n))


x = 234051


def sum_of_digits(n):
    if n < 10:
        return n
    digit = n % 10
    n = n // 10
    summ = digit + sum_of_digits(n)
    if summ >= 10:
        summ = summ // 10 + summ % 10
    return summ


print(sum_of_digits(x))
