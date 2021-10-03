# # Core Function/s ------------------------------------------------------------
# def get_number_metadata(number):
#     odd_count, even_count = no_of_odd_and_even_digits(number)
#
#     number_metadata = (
#         odd_count,
#         even_count,
#         no_of_digits(number),
#         sum_of_digits(number),
#         actual_value(number)
#     )
#
#     return number_metadata
#
#
# # In this case, zero (i.e., 0) is counted as
# # an even number.
# def no_of_odd_and_even_digits(number):
#     pure_numbers = get_pure_numbers(number)
#
#     odd_count, even_count = 0, 0
#     for digit in pure_numbers:
#         # if int(digit) == 0:
#         #     continue
#
#         if int(digit) % 2 == 1:
#             odd_count += 1
#         else:
#             even_count += 1
#
#     return odd_count, even_count
#
#
# # Trailing zeroes on the decimal part is counted.
# def no_of_digits(number):
#     if number.find('.') == -1:
#         return len(number)
#     else:
#         return len(number) - 1
#
#
# def sum_of_digits(number):
#     pure_numbers = get_pure_numbers(number)
#
#     total_sum = 0
#     for digit in pure_numbers:
#         total_sum += int(digit)
#
#     return total_sum
#
#
# def actual_value(number):
#     return float(number)
# # End of Core Functions ------------------------------------------------------
#
#
# # Helper Function/s ----------------------------------------------------------
# def get_pure_numbers(number):
#     float_number = actual_value(number)
#     pure_numbers = str(float_number).replace('.', '')
#
#     return pure_numbers
# # End of Helper Function/s ---------------------------------------------------
#
#
# if __name__ == '__main__':
#     numbers = [
#         '9.80',
#         '2.45',
#         '3.73',
#         '7.10',
#         '9.13',
#         '3.58',
#         '3.51',
#         '4.21',
#         '6.50',
#         '9.94'
#     ]
#
#     print(numbers)
#
#     # Get all the numbers' metadata.
#     numbers_metadata = []
#     for number in numbers:
#         numbers_metadata.append(get_number_metadata(number))
#
#     # Sort the numbers
#     numbers_metadata.sort(key=lambda no_metadata: (no_metadata[0],
#                                                    no_metadata[1],
#                                                    no_metadata[2],
#                                                    no_metadata[3],
#                                                    no_metadata[4]))
#
#     # Print the sorted floating point number.
#     for no_metadata in numbers_metadata:
#         print(float(no_metadata[4]))


# Core Function/s ------------------------------------------------------------
def get_number_metadata(number):
    odd_count, even_count = no_of_odd_and_even_digits(number)

    number_metadata = (
        odd_count,
        even_count,
        no_of_digits(number),
        sum_of_digits(number),
        actual_value(number)
    )

    return number_metadata


# In this case, zero (i.e., 0) is counted as
# an even number.
def no_of_odd_and_even_digits(number):
    pure_numbers = get_pure_numbers(number)

    odd_count, even_count = 0, 0
    for digit in pure_numbers:
        # if int(digit) == 0:
        #     continue

        if int(digit) % 2 == 1:
            odd_count += 1
        else:
            even_count += 1

    return odd_count, even_count


# Trailing zeroes on the decimal part is counted.
def no_of_digits(number):
    if number.find('.') == -1:
        return len(number)
    else:
        return len(number) - 1


def sum_of_digits(number):
    pure_numbers = get_pure_numbers(number)

    total_sum = 0
    for digit in pure_numbers:
        total_sum += int(digit)

    return total_sum


def actual_value(number):
    return float(number)
# End of Core Functions ------------------------------------------------------


# Helper Function/s ----------------------------------------------------------
def get_pure_numbers(number):
    float_number = actual_value(number)
    pure_numbers = str(float_number).replace('.', '')

    return pure_numbers
# End of Helper Function/s ---------------------------------------------------


if __name__ == '__main__':
    # Get the number input/s.
    no_of_numbers = int(input())
    numbers = []

    for _ in range(no_of_numbers):
        numbers.append(input())

    # Get all the numbers' metadata.
    numbers_metadata = []
    for number in numbers:
        numbers_metadata.append(get_number_metadata(number))

    # Sort the numbers
    numbers_metadata.sort(key=lambda no_metadata: (no_metadata[0],
                                                   no_metadata[1],
                                                   no_metadata[2],
                                                   no_metadata[3],
                                                   no_metadata[4]))

    # Print the sorted floating point number.
    for no_metadata in numbers_metadata:
        print(float(no_metadata[4]))
