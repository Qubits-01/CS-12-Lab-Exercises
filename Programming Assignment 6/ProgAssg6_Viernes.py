def main():
    cipher = {
        "01": '1',
        "10": '2',
        "100": '3',
        "111": '4',
        "101": '5',
        "011": '6',
        "1010": '7',
        "11111": '8',
        "11011": '9'
    }

    msg = '011010110'
    answers = []

    output = decode(msg, cipher, answers)
    print('\noutput')

    for answer in sorted(answers):
        print(answer)


def decode(msg, cipher, all_ans, ans=[]):
    # Base case/s.
    if len(msg) == 0:
        print('end', ans)
        all_ans.append(''.join(ans))
        return True

    # Find all possible code/s.
    possible_codes = []
    for max_len in range(2, len(msg)+1):
        if max_len > 5:
            break

        code = msg[:max_len]

        if code in cipher:
            possible_codes.append(code)
        else:
            pass

    # Decode all possible code/s.
    if len(possible_codes) > 0:
        print(possible_codes, msg)

        for i in range(len(possible_codes)):
            code = possible_codes[i]
            ans.append(cipher[code])

            if decode(msg[len(code):], cipher, all_ans, ans):
                # Clean ans for the next decoded message.
                ans.pop()

        # Clean ans for the next decoded message.
        if len(ans) > 0:
            ans.pop()
            return False
    else:
        # Backtrack if msg is invalid.
        if len(ans) > 0:
            ans.pop()
            return False


if __name__ == '__main__':
    main()


# def main():
#     cipher = {
#         "01": '1',
#         "10": '2',
#         "100": '3',
#         "111": '4',
#         "101": '5',
#         "011": '6',
#         "1010": '7',
#         "11111": '8',
#         "11011": '9'
#     }
#
#     msg = input()
#     answers = []
#
#     decode(msg, cipher, answers)
#
#     for answer in sorted(answers):
#         print(answer)
#
#
# def decode(msg, cipher, all_ans, ans=[]):
#     # Base case/s.
#     if len(msg) == 0:
#         all_ans.append(''.join(ans))
#         return True
#
#     possible_codes = []
#     for max_len in range(2, len(msg) + 1):
#         if max_len > 5:
#             break
#
#         code = msg[:max_len]
#         if code in cipher:
#             possible_codes.append(code)
#
#     if len(possible_codes) > 0:
#         for i in range(len(possible_codes)):
#             code = possible_codes[i]
#             ans.append(cipher[code])
#
#             if decode(msg[len(code):], cipher, all_ans, ans):
#                 # Clean ans for the next decoded message.
#                 ans.pop()
#
#         # Clean ans for the next decoded message.
#         if len(ans) > 0:
#             ans.pop()
#     else:
#         # Backtrack if msg is invalid.
#         if len(ans) > 0:
#             ans.pop()
#             return False
#
#
# if __name__ == '__main__':
#     main()
