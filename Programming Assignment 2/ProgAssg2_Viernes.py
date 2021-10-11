def main():
    n_val = 5
    n_ids = [
        '1991-59171',
        '1995-64380',
        '1990-06115',
        '1990-46072',
        '1991-72199'
    ]
    m_val = 50
    m_ids = [
        '1991-36595',
        '1992-99478',
        '1993-37931',
        '1991-71420',
        '1994-08983',
        '1995-51944',
        '1990-02607',
        '1991-32236',
        '1995-93290',
        '1992-92176',
        '1992-75394',
        '1992-82179',
        '1993-31238',
        '1992-75100',
        '1991-30609',
        '1994-32431',
        '1992-93196',
        '1993-89594',
        '1994-02639',
        '1992-36112',
        '1990-67513',
        '1994-78037',
        '1990-80622',
        '1991-06519',
        '1991-11999',
        '1991-29072',
        '1995-80148',
        '1992-30573',
        '1995-46456',
        '1995-13129',
        '1990-71715',
        '1990-05333',
        '1993-79602',
        '1992-73086',
        '1994-16961',
        '1995-31348',
        '1995-37748',
        '1995-15103',
        '1993-57031',
        '1993-03072',
        '1992-99881',
        '1994-73003',
        '1994-78172',
        '1992-01608',
        '1992-95972',
        '1990-18533',
        '1990-90847',
        '1994-79273',
        '1992-88265',
        '1990-59747'
    ]

    n_ids = [n_id.split('-') for n_id in n_ids]
    m_ids = [m_id.split('-') for m_id in m_ids]

    all_ids = n_ids + m_ids
    all_ids.sort(key=lambda mn_id: (mn_id[0], mn_id[1]))
    print(all_ids)

    partitioned_ids = {}
    for mn_id in all_ids:
        if mn_id[0] in partitioned_ids:
            partitioned_ids[mn_id[0]].append(mn_id[1])
        else:
            partitioned_ids[mn_id[0]] = [mn_id[1]]

    print(partitioned_ids)

    for n_id in n_ids:
        print(f'{n_id[0]}-{n_id[1]} {binary_search(partitioned_ids[n_id[0]], n_id[1])+1}')


def binary_search(array, to_search):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == to_search:
            return mid
        elif array[mid] < to_search:
            left = mid + 1
        else:
            right = mid - 1

    return -1

    # left = 0
    # mid = 0
    # right = len(array) - 1
    #
    # while left <= right:
    #     mid = (left + right) // 2
    #
    #     if array[mid] < to_search:
    #         left = mid + 1
    #     elif array[mid] > to_search:
    #         right = mid - 1
    #     else:
    #         return mid
    #
    # return -1


if __name__ == '__main__':
    main()


# def main():
#     n_val = int(input())
#     n_ids = []
#
#     for _ in range(n_val):
#         n_ids.append(input().split('-'))
#
#     m_val = int(input())
#     m_ids = []
#
#     for _ in range(m_val):
#         m_ids.append(input().split('-'))
#
#     all_ids = n_ids + m_ids
#     all_ids.sort(key=lambda mn_id: (mn_id[0], mn_id[1]))
#
#     partitioned_ids = {}
#     for mn_id in all_ids:
#         if mn_id[0] in partitioned_ids:
#             partitioned_ids[mn_id[0]].append(mn_id[1])
#         else:
#             partitioned_ids[mn_id[0]] = [mn_id[1]]
#
#     for n_id in n_ids:
#         print(f'{n_id[0]}-{n_id[1]} {binary_search(partitioned_ids[n_id[0]], n_id[1])+1}')
#
#
# def binary_search(array, to_search):
#     left = 0
#     right = len(array) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#
#         if array[mid] == to_search:
#             return mid
#         elif array[mid] < to_search:
#             left = mid + 1
#         else:
#             right = mid - 1
#
#     return -1
#
#     # left = 0
#     # mid = 0
#     # right = len(array) - 1
#     #
#     # while left <= right:
#     #     mid = (left + right) // 2
#     #
#     #     if array[mid] < to_search:
#     #         left = mid + 1
#     #     elif array[mid] > to_search:
#     #         right = mid - 1
#     #     else:
#     #         return mid
#     #
#     # return -1
#
#
# if __name__ == '__main__':
#     main()
