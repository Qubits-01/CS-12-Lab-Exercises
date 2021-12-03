def main():
    ns = [
        [20.45, 88.76],
        [35.35, 80.16],
        [7.98, 49.30],
        [55.44, 4.73],
        [89.48, 53.33],
        [76.77, 93.76],
        [54.33, 13.16],
        [46.93, 40.00],
        [37.28, 87.48],
        [29.70, 57.31]
    ]
    ms = [
        [15.58, 52.26],
        [86.49, 13.15],
        [97.57, 0.06]
    ]

    largest = 0

    q = 0
    l = 0

    for n1 in ns:
        l += 1

        for n2 in ns[l:]:
            r2 = (n1[0] - n2[0]) ** 2 + (n1[1] - n2[1]) ** 2

            if r2 < largest:
                continue


            for m in ms:
                q += 1

                is_in1 = ((m[0] - n1[0]) ** 2) + ((m[1] - n1[1]) ** 2) <= r2

                if is_in1:
                    break

                if m == ms[-1]:
                    if r2 > largest:
                        largest = r2

            for m in ms:
                q += 1

                is_in2 = ((m[0] - n2[0]) ** 2) + ((m[1] - n2[1]) ** 2) <= r2

                if is_in2:
                    break

                if m == ms[-1]:
                    if r2 > largest:
                        largest = r2

    print(largest ** (1 / 2))
    print(q)


if __name__ == '__main__':
    main()


# v1.1.
# def main():
#     ms = []
#     m = int(input())
#
#     for _ in range(m):
#         ms.append([float(coord) for coord in input().split(',')])
#
#     ns = []
#     n = int(input())
#
#     for _1 in range(n):
#         ns.append([float(coord) for coord in input().split(',')])
#
#     largest = 0
#
#     for i in range(n):
#         for j in range(n - i - 1):
#             p1 = ns[i]
#             p2 = ns[j + i + 1]
#             r2 = ((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2)
#
#             if r2 < largest:
#                 continue
#
#             for m in ms:
#                 is_in1 = ((m[0] - p1[0]) ** 2) + ((m[1] - p1[1]) ** 2) <= r2
#
#                 if is_in1:
#                     break
#
#                 if m == ms[-1]:
#                     if r2 > largest:
#                         largest = r2
#
#             for m in ms:
#                 is_in2 = ((m[0] - p2[0]) ** 2) + ((m[1] - p2[1]) ** 2) <= r2
#
#                 if is_in2:
#                     break
#
#                 if m == ms[-1]:
#                     if r2 > largest:
#                         largest = r2
#
#     print(largest ** (1 / 2))
#
#
# if __name__ == '__main__':
#     main()


# v1.2.
# def main():
#     ms = []
#     m = int(input())
#
#     for _ in range(m):
#         ms.append([float(coord) for coord in input().split(',')])
#
#     ns = []
#     n = int(input())
#
#     for _1 in range(n):
#         ns.append([float(coord) for coord in input().split(',')])
#
#     largest = 0
#
#     for i in range(n):
#         for j in range(n - i - 1):
#             p1 = ns[i]
#             p2 = ns[j + i + 1]
#             r2 = ((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2)
#
#             if r2 < largest:
#                 continue
#
#             is1_valid, is2_valid = True, True
#             is_in1, is_in2 = False, False
#
#             for m in ms:
#                 if is1_valid:
#                     is_in1 = ((m[0] - p1[0]) ** 2) + ((m[1] - p1[1]) ** 2) <= r2
#
#                 if is2_valid:
#                     is_in2 = ((m[0] - p2[0]) ** 2) + ((m[1] - p2[1]) ** 2) <= r2
#
#                 if is_in1 and is_in2:
#                     break
#
#                 if is_in1:
#                     is1_valid = False
#                     is_in1 = True
#
#                 if is_in2:
#                     is2_valid = False
#                     is_in2 = True
#
#                 if m == ms[-1]:
#                     if r2 > largest:
#                         largest = r2
#
#     print(largest ** (1 / 2))
#
#
# if __name__ == '__main__':
#     main()


# 1.3.
# def main():
#     ms = []
#     m = int(input())
#
#     for _ in range(m):
#         ms.append([float(coord) for coord in input().split(',')])
#
#     ns = []
#     n = int(input())
#
#     for _1 in range(n):
#         ns.append([float(coord) for coord in input().split(',')])
#
#     largest = 3750
#
#     l = 0
#
#     for n1 in ns:
#         l += 1
#
#         for n2 in ns[l:]:
#             r2 = (n1[0] - n2[0]) ** 2 + (n1[1] - n2[1]) ** 2
#
#             if r2 < largest:
#                 continue
#
#             for m in ms:
#                 is_in1 = ((m[0] - n1[0]) ** 2) + ((m[1] - n1[1]) ** 2) <= r2
#
#                 if is_in1:
#                     break
#
#                 if m == ms[-1]:
#                     if r2 > largest:
#                         largest = r2
#
#             for m in ms:
#                 is_in2 = ((m[0] - n2[0]) ** 2) + ((m[1] - n2[1]) ** 2) <= r2
#
#                 if is_in2:
#                     break
#
#                 if m == ms[-1]:
#                     if r2 > largest:
#                         largest = r2
#
#     print(largest ** (1 / 2))
#
#
# if __name__ == '__main__':
#     main()
