# Write a recursive function to count all the elements in a list (divide and rule).

list_to_sum = [1, 2, 3, 4, 12]


def count_list(array):
    if len(array) == 1:
        return array[0]
    else:
        return array[0] + count_list(array[1:])


print(count_list(list_to_sum))

# Find the biggest number in the list (divide and rule).

numbers_list = [2, 5, 8, 3, -22, 17]


def biggest_number(array):
    if len(array) == 1:
        return array[0]
    else:
        return max(array[0], biggest_number(array[1:]))


print(biggest_number(numbers_list))

