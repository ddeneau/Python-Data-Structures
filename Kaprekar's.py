import random
import time
import matplotlib

#  Count the number of steps it takes to get to the Kaprekar Constant (6174) from any numbers, four
#  digits or less, with at least two unique numbers.
KAPREKAR_CONSTANT = 6174


def count_iterations(n):
    print(kaprekar(n))


# Function for computing 6174.
def kaprekar(number_in):
    current_number = number_in
    iterations = 0
    record = list()

    while current_number != KAPREKAR_CONSTANT:
        digits = separate_digits(current_number)
        ascending = sorted(digits)
        descending = sorted(digits)
        descending = reverse_digits(descending)
        current_number = subtract_list(ascending, descending)
        print("i=" + str(iterations) + ": " + str(current_number))
        iterations += 1

    return "Iterations " + str(iterations)


# Splits a number into a list of digits.
def separate_digits(number):
    new_list = list()
    number_string = str(number)

    for char in number_string:
        new_list.append(int(char))

    return new_list


# Sorts an array.
def sort(digits):
    new_list = list()
    max_value = 0
    max_found = False

    for i in range(len(digits)):
        current_value = digits[i]

        if i == len(digits) - 1:
            new_list.append(digits[i])
            if max_found:
                new_list.append(max_value)
        elif current_value > digits[i + 1]:
            max_value = current_value
            max_found = True
            continue
        else:
            new_list.append(digits[i])

    return new_list


# Reverses an array.
def reverse_digits(digits):
    new_list = list()

    for i in range(len(digits)):
        new_list.append(digits[((len(digits) - 1) - i)])

    while len(new_list) < 4:
        new_list.insert((len(new_list)), 0)

    return new_list


# Sums two numbers as lists.
def subtract_list(list_ascending, list_descending):
    ascending_string = ""
    descending_string = ""

    for i in range(len(list_ascending)):
        ascending_string += str(list_ascending[i])

    for i in range(len(list_descending)):
        descending_string += str(list_descending[i])

    ascending = int(ascending_string)
    descending = int(descending_string)

    return descending - ascending

#
#
# TESTS BELOW
#
#


# Main test function.
def test_runtime(batch_size, min_size, max_size):
    record = list()

    for i in range(batch_size):
        test_number = generate_number(random.randrange(min_size, max_size))
        print(str(test_number))
        start = 0
        count_iterations(test_number)
        stop = time.process_time_ns()
        print("t = " + str(stop - start) + "ns.  ")
        record.append(stop - start)

    return record


# Generates random numbers of length passed in through the parameter.
def generate_number(digits):
    number_string = ""

    while has_two_unique(number_string):
        for i in range(digits):
            number_string += str(random.randrange(1, 9))

    return int(number_string)


# Returns true if the number passed through the parameter has 2 or more unique digits, and false otherwise.
def has_two_unique(number_string):
    unique = 0

    if number_string.__eq__(""):
        return True

    for char in number_string:
        current_number = int(char)
        for other_char in number_string:
            other_number = int(char)
            if current_number == other_number:
                continue
            else:
                unique += 1

    return True if unique >= 2 else False


kaprekar(12)
print()
kaprekar(412)
print()
kaprekar(319)
print()
kaprekar(347)
print()
kaprekar(98)



