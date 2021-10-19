def main():
    contestants = [1,2,3,4,5]
    r = 2

    print(spin_r2(contestants, r))


def spin_r2(contestants, r):
    # Organize recursive data.
    if contestants.count(None) == 0:
        contestants.append(0)

    size = len(contestants) - 1

    # Base case.
    if contestants.count(None) == (size - 1):
        for i in range(size):
            if contestants[i] is not None:
                return i + 1

    # Update recursive data.
    c_index = contestants[-1]
    contestants = contestants[:size]
    count = 0

    # Recursive step.
    while count < r:
        if contestants[c_index] is not None:
            count += 1
            c_index = (c_index + 1) % size
        else:
            c_index = (c_index + 1) % size

        if count == r:
            contestants[c_index - 1] = None
            contestants.append(c_index)

            return spin_r2(contestants, r)


# def spin_r1(contestants, r):
#     size = len(contestants)
#
#     # Base case/s.
#     # if size == 1:
#     #     return 1
#     #
#     # if r == 1:
#     #     return size
#
#     if contestants.count(None) == (size - 1):
#         for i in range(size):
#             if contestants[i] is not None:
#                 return i + 1
#
#     c_index = 0
#
#     # Eliminate players (size - 1) times.
#     for i in range(size - 1):
#         count = 0
#
#         while count < r:
#             if contestants[c_index] is not None:
#                 count += 1
#                 c_index = (c_index + 1) % size
#             else:
#                 c_index = (c_index + 1) % size
#
#             if count == r:
#                 contestants[c_index - 1] = None
#
#     return spin_r1(contestants, r)


# def spin_i(contestants, r):
#     size = len(contestants)
#     c_index = 0
#
#     # Eliminate players (size - 1) times.
#     for i in range(size-1):
#         count = 0
#
#         while count < r:
#             if contestants[c_index] is not None:
#                 count += 1
#                 c_index = (c_index + 1) % size
#             else:
#                 c_index = (c_index + 1) % size
#
#             if count == r:
#                 contestants[c_index-1] = None
#
#     # print(contestants)
#
#     for i in range(size):
#         if contestants[i] is not None:
#             return i + 1


if __name__ == '__main__':
    main()


'''
NOT YET FINAL

1. Implement using iteration.
2. Convert to recursion.
3. Debug
'''


def spin(contestants, r):
    size = len(contestants)

    # Base case/s.
    if contestants.count(None) == (size - 1):
        for i in range(size):
            if contestants[i] is not None:
                return i + 1

    c_index = 0

    # Eliminate players (size - 1) times.
    for i in range(size - 1):
        count = 0

        while count < r:
            if contestants[c_index] is not None:
                count += 1
                c_index = (c_index + 1) % size
            else:
                c_index = (c_index + 1) % size

            if count == r:
                contestants[c_index - 1] = None

    return spin(contestants, r)
