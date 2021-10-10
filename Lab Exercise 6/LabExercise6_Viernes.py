def main():
    no_of_test_cases = int('2')
    first_webpage = 'https://www.helloworld.com'
    commands_1 = [
        'dump',
        'https://www.abcdef.com',
        'https://www.reddit.com',
        'back',
        'dump',
        'https://www.test.com'
    ]
    commands_2 = [
        'dump',
        'dump',
        'back',
        'dump'
    ]

    history = [first_webpage]

    for command in commands_1:
        if command == 'dump':
            print(dump(history))
        elif command == 'back':
            back(history)
        else:
            go(history, command)

    # print('TC1\n', history)

    history = [dump(history)]

    for command in commands_2:
        if command == 'dump':
            print(dump(history))
        elif command == 'back':
            back(history)
        else:
            go(history, command)

    # print('TC2\n', history)


def dump(history):
    return history[-1]


def back(history):
    if len(history) > 1:
        history.pop()


def go(history, url):
    if url != history[-1]:
        history.append(url)


if __name__ == '__main__':
    main()


# def main():
#     no_of_test_cases = int(input())
#     history = [input()]
#
#     for _ in range(no_of_test_cases):
#         no_of_commands = int(input())
#
#         for _ in range(no_of_commands):
#             command = input()
#
#             if command == 'dump':
#                 print(dump(history))
#             elif command == 'back':
#                 back(history)
#             else:
#                 go(history, command)
#
#         history = [dump(history)]
#
#
# def dump(history):
#     return history[-1]
#
#
# def back(history):
#     if len(history) > 1:
#         history.pop()
#
#
# def go(history, url):
#     if url != history[-1]:
#         history.append(url)
#
#
# if __name__ == '__main__':
#     main()
