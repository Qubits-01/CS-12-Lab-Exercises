def main():
    n_test_cases = 2

    pattern_1 = '%$'

    a_to_f = ['a', 'b', 'c', 'd', 'e', 'f']
    big_a_to_f = ['A', 'B', 'C', 'D', 'E', 'F']
    zero_9 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    output_strings = []

    # Calculate the character element counts
    # (metadata). Needed for the actual enumeration
    # of characters based on the given pattern.
    str_count = []
    for char in pattern_1:
        if char == '$':
            str_count.append(10)
        else:
            str_count.append(6)

    for i in range(len(str_count)):
        for j in range(i+1, len(pattern_1)):
            str_count[i] = str_count[i] * str_count[j]

    print(str_count)

    str_outputs = []
    for i in range(len(pattern_1)):
        # When there is only 1 character in the given pattern.
        if len(str_count) == 1:
            if pattern_1[i] == '#':
                enum_1_elem(str_outputs, str_count, a_to_f)
            elif pattern_1[i] == '$':
                enum_1_elem(str_outputs, str_count, zero_9)
            else:
                enum_1_elem(str_outputs, str_count, big_a_to_f)

        # When there is > 1 characters in given the pattern.
        else:
            # When enumerating the 1st character in the given pattern.
            if i == 0:
                if pattern_1[i] == '#':
                    for j in range(6):
                        for _ in range(str_count[i+1]):
                            str_outputs.append(a_to_f[j])
                elif pattern_1[i] == '$':
                    for j in range(10):
                        for _ in range(str_count[i + 1]):
                            str_outputs.append(str(j))
                else:
                    for j in range(6):
                        for _ in range(str_count[i + 1]):
                            str_outputs.append(a_to_f[j].upper())

            # When enumerating the 2nd, 3rd, ..., len(pattern) characters
            # in the given pattern.
            else:
                # When enumerating the last character in the given pattern.
                if i != (len(pattern_1) - 1):
                    if pattern_1[i] == '#':
                        temp_i = 0

                        for j in range(0, str_count[0], str_count[i + 1]):
                            for k in range(str_count[i + 1]):
                                str_outputs[j + k] = str_outputs[j + k] + a_to_f[temp_i]

                            temp_i += 1

                            if temp_i == 6:
                                temp_i = 0
                    elif pattern_1[i] == '$':
                        temp_i = 0

                        for j in range(0, str_count[0], str_count[i + 1]):
                            for k in range(str_count[i + 1]):
                                str_outputs[j + k] = str_outputs[j + k] + str(temp_i)

                            temp_i += 1

                            if temp_i == 10:
                                temp_i = 0
                    else:
                        temp_i = 0

                        for j in range(0, str_count[0], str_count[i+1]):
                            for k in range(str_count[i+1]):
                                str_outputs[j+k] = str_outputs[j+k] + a_to_f[temp_i].upper()

                            temp_i += 1

                            if temp_i == 6:
                                temp_i = 0

                # When not enumerating the last character in the given pattern.
                else:
                    if pattern_1[i] == '#':
                        for j in range(str_count[0]):
                            str_outputs[j] = str_outputs[j] + a_to_f[j % 6]
                    elif pattern_1[i] == '$':
                        for j in range(str_count[0]):
                            str_outputs[j] = str_outputs[j] + str(j % 10)
                    else:
                        for j in range(str_count[0]):
                            str_outputs[j] = str_outputs[j] + a_to_f[j % 6].upper()

    print(len(str_outputs), str_outputs)

    # Print the enumerated strings based on the given pattern.
    for str_output in str_outputs:
        print(str_output)


def enum_1_elem(str_outputs, str_count, source_set):
    for j in range(str_count[0]):
        str_outputs.append(source_set[j])


if __name__ == '__main__':
    main()


# def main():
#     n_test_cases = int(input())
#     a_to_f = ['a', 'b', 'c', 'd', 'e', 'f']
#
#     for _ in range(n_test_cases):
#         pattern_1 = input()
#         output_strings = []
#
#         str_count = []
#         for char in pattern_1:
#             if char == '$':
#                 str_count.append(10)
#             else:
#                 str_count.append(6)
#
#         for i in range(len(str_count)):
#             for j in range(i+1, len(pattern_1)):
#                 str_count[i] = str_count[i] * str_count[j]
#
#         str_outputs = []
#         for i in range(len(pattern_1)):
#             if len(str_count) == 1:
#                 if pattern_1[i] == '#':
#                     for j in range(str_count[0]):
#                         str_outputs.append(a_to_f[j])
#                 elif pattern_1[i] == '$':
#                     for j in range(str_count[0]):
#                         str_outputs.append(str(j))
#                 else:
#                     for j in range(str_count[0]):
#                         str_outputs.append(a_to_f[j].upper())
#             else:
#                 if i == 0:
#                     if pattern_1[i] == '#':
#                         for j in range(6):
#                             for _ in range(str_count[i+1]):
#                                 str_outputs.append(a_to_f[j])
#                     elif pattern_1[i] == '$':
#                         for j in range(10):
#                             for _ in range(str_count[i + 1]):
#                                 str_outputs.append(str(j))
#                     else:
#                         for j in range(6):
#                             for _ in range(str_count[i + 1]):
#                                 str_outputs.append(a_to_f[j].upper())
#                 else:
#                     if i != (len(pattern_1) - 1):
#                         if pattern_1[i] == '#':
#                             temp_i = 0
#
#                             for j in range(0, str_count[0], str_count[i + 1]):
#                                 for k in range(str_count[i + 1]):
#                                     str_outputs[j + k] = str_outputs[j + k] + a_to_f[temp_i]
#
#                                 temp_i += 1
#
#                                 if temp_i == 6:
#                                     temp_i = 0
#                         elif pattern_1[i] == '$':
#                             temp_i = 0
#
#                             for j in range(0, str_count[0], str_count[i + 1]):
#                                 for k in range(str_count[i + 1]):
#                                     str_outputs[j + k] = str_outputs[j + k] + str(temp_i)
#
#                                 temp_i += 1
#
#                                 if temp_i == 10:
#                                     temp_i = 0
#                         else:
#                             temp_i = 0
#
#                             for j in range(0, str_count[0], str_count[i+1]):
#                                 for k in range(str_count[i+1]):
#                                     str_outputs[j+k] = str_outputs[j+k] + a_to_f[temp_i].upper()
#
#                                 temp_i += 1
#
#                                 if temp_i == 6:
#                                     temp_i = 0
#                     else:
#                         if pattern_1[i] == '#':
#                             for j in range(str_count[0]):
#                                 str_outputs[j] = str_outputs[j] + a_to_f[j % 6]
#                         elif pattern_1[i] == '$':
#                             for j in range(str_count[0]):
#                                 str_outputs[j] = str_outputs[j] + str(j % 10)
#                         else:
#                             for j in range(str_count[0]):
#                                 str_outputs[j] = str_outputs[j] + a_to_f[j % 6].upper()
#
#         for str_output in str_outputs:
#             print(str_output)
#
#
# if __name__ == '__main__':
#     main()
