# Sum of odd numbers
def sum_of_odd_numbers(number):
    return number**3


print(sum_of_odd_numbers(4))

# When given a list, the program should return a list of all the elements that are below the arithmetical mean of the
# original list.  The arithmetical mean is the sum of all elements divided by the number of elements.
number_list = [2, 4, 3, 1, 0, 2, 0, 0, 15]


def arithmetical_mean(n):
    result = []
    max_number = int(sum(n)/len(n))
    for i in n:
        if i < max_number:
            result.append(i)
    return result


print(arithmetical_mean(number_list))

# When given a list of elements find the two lowest elements. They can be equal to each other or different.
number_list = [29, 34, 32, 15, 17, 112, 25, 20, 15]


def two_lowest_elements(array):
    result = sorted(array)
    return result[:2]


print(two_lowest_elements(number_list))
