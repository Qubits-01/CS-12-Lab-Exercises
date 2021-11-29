def main():
    prices_raw = '13 25 30 33 38 41 43 43 44 55 67 69'
    # prices_raw = '2 4 6 8 10'
    prices_lst = [int(price) for price in prices_raw.split()]
    prices_lst.sort()
    prices_set = set(prices_lst)
    budget = 136

    print(f'{prices_lst} \n{prices_set}')

    print(solve(prices_lst, prices_set, budget))


def solve(prices_lst, prices_set, budget):
    seed = search(prices_lst, budget // 2)

    if prices_lst[seed+1] == (budget // 2):
        seed += 1

    while True:
        diff = budget - prices_lst[seed]

        if diff in prices_set:
            if prices_lst[seed] > diff:
                return diff, prices_lst[seed]
            else:
                return prices_lst[seed], diff
        else:
            seed -= 1


def search(arr, n):
    # Returns the index of the largest element in arr
    # that is less than the value of n.

    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2

        if n < arr[mid]:
            right = mid
        else:
            left = mid + 1

    if arr[left-1] == n:
        left -= 1

    return left - 1


if __name__ == '__main__':
    main()


# def main():
#     prices_lst = [int(price) for price in input().split()]
#     prices_lst.sort()
#     prices_set = set(prices_lst)
#     budget = int(input())
#
#     print(solve(prices_lst, prices_set, budget))
#
#
# def solve(prices_lst, prices_set, budget):
#     seed = search(prices_lst, budget // 2)
#
#     if prices_lst[seed + 1] == (budget // 2):
#         seed += 1
#
#     while True:
#         diff = budget - prices_lst[seed]
#
#         if diff in prices_set:
#             if prices_lst[seed] > diff:
#                 return diff, prices_lst[seed]
#             else:
#                 return prices_lst[seed], diff
#         else:
#             seed -= 1
#
#
# def search(arr, n):
#     # Returns the index of the largest element in arr
#     # that is less than the value of n.
#
#     left = 0
#     right = len(arr)
#
#     while left < right:
#         mid = (left + right) // 2
#
#         if n < arr[mid]:
#             right = mid
#         else:
#             left = mid + 1
#
#     if n[left - 1] == n:
#         left -= 1
#
#     return left - 1
#
#
# if __name__ == '__main__':
#     main()
