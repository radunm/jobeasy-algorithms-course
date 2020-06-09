# Sum of 3 modified
# Rewrite a program with any number of digits.
#  Instead of  3 digits, you should sum digits up from n digits number,
#  Where  User enters n manually. n > 0

from random import randint

min_rand = 1
max_rand = "9"
result = 0

digit = int(input("Please, enter digit: "))

digit -= 1

while digit > 0:
    min_rand *= 10
    max_rand += "9"
    digit -= 1

max_rand = int(max_rand)

random_number = randint(min_rand, max_rand)
print(f'Random number {random_number}')


while random_number > 0:
    result = result + (random_number % 10)
    random_number = random_number // 10

print(f"Sum: {result}")


# Find max number from 3 values, entered manually from a keyboard

one = int(input("Enter first digit: "))
two = int(input("Enter second digit: "))
three = int(input("Enter third digit: "))


def compare(x, y, z):
    if x > y:
        if x > z:
            return x
        else:
            return z
    else:
        if y > z:
            return y
        else:
            return z


print(f"You enter {one}, {two}, {three}")

print(f"Max number {compare(one, two, three)}")


# Count odd and even numbers.  Count odd and even digits of the whole number. E.g, if entered number 34560,
# then 3 digits will be even (4, 6, and 0)  and  2 odd digits (3 and 5).

digit = abs(int(input("Enter whole number: ")))

odd = []
even = []
countodd = 0
counteven = 0

if digit != 0:
    while digit > 0:
        temp = digit % 10
        if temp % 2 == 0:
            even.append(temp)
            counteven += 1
        else:
            odd.append(temp)
            countodd += 1
        digit = digit // 10
else:
    even.append(digit)
    counteven += 1

even.reverse()
odd.reverse()

print(f"Number consist of {counteven} even digits {even} and {countodd} odd {odd}.")
