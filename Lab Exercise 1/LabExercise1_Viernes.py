# str_input = '1 2 3 3 2 1'.strip()
# list_input = str_input.split()
#
# palindrome_count = 0
# list_size = len(list_input)
#
# for start in range(list_size-1):
#     for end in range(list_size-(start+1)):
#         sublist = list_input[start: start+end+2]
#         print(sublist)
#
#         if sublist == sublist[::-1]:
#             palindrome_count += 1
#
#
# print(palindrome_count)

no_of_test_cases = int(input())

for _ in range(no_of_test_cases):
    list_of_ints = input().strip().split()

    palindrome_count = 0
    list_size = len(list_of_ints)

    # Traverse all the possible sublist that has >= 2
    # adjacent elements (also, w/ unique indices).
    for start in range(list_size - 1):
        for end in range(list_size - (start + 1)):
            sublist = list_of_ints[start: start + end + 2]

            # Use list splicing notation to
            # reverse the contents of a list.
            if sublist == sublist[::-1]:
                palindrome_count += 1

    print(palindrome_count)
