from itertools import product


def main():
    # Ex) '
    print('==========\nEx) [A, B]')
    perm = list(product([True, False], repeat=2))
    print(f'len: {len(perm)} | {perm}')

    count = int()
    for elem in perm:
        logical_expr = elem[0] or (elem[1] and (not elem[1]))
        count += 1 if logical_expr else 0

    print('count:', count)

    # a)
    print('==========\na) [A, B, C, D, E]')
    perm = list(product([True, False], repeat=5))
    print(f'len: {len(perm)} | {perm}')

    count = int()
    for elem in perm:
        logical_expr = (not elem[0]) and (not (elem[1] or (elem[2] and (not (elem[3] and elem[4])))))
        count += 1 if logical_expr else 0

    print('count:', count)

    # b)
    print('==========\nb) [A, B, C, D, E]')
    perm = list(product([True, False], repeat=5))
    print(f'len: {len(perm)} | {perm}')

    count = int()
    for elem in perm:
        logical_expr = ((elem[0] and elem[1]) and (elem[0] or elem[2])) and (elem[3] and (not (elem[2] and elem[4])))
        count += 1 if logical_expr else 0

    print('count:', count)

    # c)
    print('==========\nc) [A, B, C, D, E, F, G]')
    perm = list(product([True, False], repeat=7))
    print(f'len: {len(perm)} | {perm}')

    count = int()
    for elem in perm:
        logical_expr = (not (elem[0] or (elem[1] and (elem[2] or (not (elem[3] and (not (elem[4] or (elem[5] or elem[6])))))))))
        count += 1 if logical_expr else 0

    print('count:', count)

    # d)
    print('==========\nd) [A, B, C, D, E, F, G, H]')
    perm = list(product([True, False], repeat=8))
    print(f'len: {len(perm)} | {perm}')

    count = int()
    for elem in perm:
        logical_expr = (elem[0] and (not (elem[1] or (elem[2] and elem[3])))) or (elem[4] and (elem[5] or (not (elem[2] and (elem[6] or elem[7])))))
        count += 1 if logical_expr else 0

    print('count:', count)

    # e)
    print('==========\ne) [A, B, C, D, E, F, H, I, J]')
    perm = list(product([True, False], repeat=9))
    print(f'len: {len(perm)} | {perm}')

    count = int()
    for elem in perm:
        logical_expr = ((elem[0] and elem[1]) or (not (elem[2] or elem[3]))) and (elem[4] or (not (elem[5] and (elem[6] or (elem[7] and elem[8])))))
        count += 1 if logical_expr else 0

    print('count:', count)



if __name__ == '__main__':
    main()
