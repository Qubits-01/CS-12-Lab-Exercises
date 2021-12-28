def main():
    max_weight = 200
    items = (
        (40, 2),
        (80, 1),
        (80, 2),
        (140, 2),
        (10, 1)
    )

    n_gifts = knapsack(items, max_weight)
    print(n_gifts)


def knapsack(items, max_weight):
    table = [[0 for w in range(max_weight+1)] for j in range(len(items)+1)]

    for item in range(1, len(items)+1):
        curr_weight, curr_val = items[item-1]
        for weight in range(1, max_weight+1):
            if curr_weight > weight:
                table[item][weight] = table[item-1][weight]
            else:
                table[item][weight] = max(table[item-1][weight], table[item-1][weight-curr_weight] + curr_val)

    n_gifts = 0
    for i in range(len(items), 0, -1):
        if table[i][max_weight] != table[i-1][max_weight]:
            n_gifts += items[i-1][1]
            max_weight -= items[i-1][0]

    return n_gifts


if __name__ == '__main__':
    main()


# def main():
#     max_weight = int(input())
#     n = int(input())  # No. of people.
#
#     people = []
#     for _ in range(n):
#         temp = input().split()
#         if temp[0] == 'Nice':
#             people.append(tuple([int(temp[2]) * 2, 2]))
#         else:
#             people.append(tuple([int(temp[2]), 1]))
#     people = tuple(people)
#
#     n_gifts = knapsack(people, max_weight)
#     print(n_gifts)
#
#
# def knapsack(items, max_weight):
#     table = [[0 for w in range(max_weight + 1)] for j in range(len(items) + 1)]
#
#     for item in range(1, len(items) + 1):
#         curr_weight, curr_val = items[item - 1]
#         for weight in range(1, max_weight + 1):
#             if curr_weight > weight:
#                 table[item][weight] = table[item - 1][weight]
#             else:
#                 table[item][weight] = max(table[item - 1][weight], table[item - 1][weight - curr_weight] + curr_val)
#
#     n_gifts = 0
#     for i in range(len(items), 0, -1):
#         if table[i][max_weight] != table[i - 1][max_weight]:
#             n_gifts += items[i - 1][1]
#             max_weight -= items[i - 1][0]
#
#     return n_gifts
#
#
# if __name__ == '__main__':
#     main()
