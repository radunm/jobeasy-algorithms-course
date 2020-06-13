# Rewrite code, which will return only needed element of Fib sequence
def fibonacci(n):
    fib_1 = 1
    fib_2 = 1
    result = 0
    if n == 1:
        result = fib_1
    elif n == 2:
        result = fib_2
    counter = 0
    while counter < n - 2:
        result = fib_1 + fib_2
        fib_1, fib_2 = fib_2, result
        counter += 1
    return result


print(fibonacci(7))


# Use datetime library to solve problem Seconds to Date
import datetime


def sec_to_hms(seconds):
    return datetime.timedelta(seconds=seconds)


print(sec_to_hms(86460))

# Numbers ending with zeros are boring.
# They might be fun in your world, but not here.
# Get rid of them. Only the ending ones.
#
# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105
# Zero alone is fine, don't worry about it. Poor guy anyway


def no_zeros(n):
    negative = False
    if n < 0:
        negative = True
    n = abs(n)
    while n >= 10:
        zero = n % 10
        if zero == 0:
            n //= 10
        else:
            break
    if negative:
        return -n
    else:
        return n


print(no_zeros(1050))


# Given n, take the sum of the digits of n.
# If that value has more than one digit, continue reducing in this way until a single-digit number is produced.
# This is only applicable to the natural numbers.

# 16  -->  1 + 6 = 7
# 942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

def sum_of_digits(n):
    summ = 0
    while n >= 10:
        summ += n % 10
        if summ >= 10:
            summ = summ // 10 + summ % 10
        n = n // 10
    summ += n
    summ = summ // 10 + summ % 10
    return summ


print(sum_of_digits(493193))
