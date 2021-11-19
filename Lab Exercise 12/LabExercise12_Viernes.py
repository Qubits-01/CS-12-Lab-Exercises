def main():
    schools = [3, 4, 5, 6, 7, 8, 9, 10]
    dorms = [1, 1, 1, 1, 1, 1, 1, 1]
    targets = [15, 329, 32, 70, 89]

    r2s = []
    for i in range(0, len(schools), 2):
        r2s.append(get_r2(schools[i], schools[i+1], dorms[i], dorms[i+1]))

    for target in targets:
        print(search(r2s, target))


def get_r2(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def search(r2s, target):
    # Returns the index of the largest element in r2s
    # that is less than the value of target.

    left = 0
    right = len(r2s)

    while left < right:
        mid = (left + right) // 2

        if target < r2s[mid]:
            right = mid
        else:
            left = mid + 1

    if r2s[left-1] == target:
        left -= 1

    return left - 1


if __name__ == '__main__':
    main()


# def main():
#     no_tc = int(input())
#     for _ in range(no_tc):
#         schools = [int(elem) for elem in input().split()]
#         dorms = [int(elem) for elem in input().split()]
#         targets = [int(elem) for elem in input().split()]
#
#         r2s = []
#         for i in range(0, len(schools), 2):
#             r2s.append(get_r2(schools[i], schools[i + 1], dorms[i], dorms[i + 1]))
#
#         for target in targets:
#             print(search(r2s, target))
#
#
# def get_r2(x1, y1, x2, y2):
#     return (x1 - x2) ** 2 + (y1 - y2) ** 2
#
#
# def search(r2s, target):
#     # Returns the index of the largest element in r2s
#     # that is less than the value of target.
#
#     left = 0
#     right = len(r2s)
#
#     while left < right:
#         mid = (left + right) // 2
#
#         if target < r2s[mid]:
#             right = mid
#         else:
#             left = mid + 1
#
#     if r2s[left - 1] == target:
#         left -= 1
#
#     return left - 1
#
#
# if __name__ == '__main__':
#     main()
