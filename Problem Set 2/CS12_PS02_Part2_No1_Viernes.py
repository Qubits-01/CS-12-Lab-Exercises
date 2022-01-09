from itertools import product


def main():
    # Ex) '
    print('==========\nEx) [A, B]')
    perm = list(product([True, False], repeat=2))
    print(f'len: {len(perm)} | {perm}')

    count = int()
    for elem in perm:
        A, B = elem
        logical_expr = A or (B and (not B))
        count += 1 if logical_expr else 0

    print('count:', count)

    # a)
    print('==========\na) [A, B, C, D, E]')
    perm = list(product([True, False], repeat=5))
    print(f'len: {len(perm)} | {perm}')

    count = int()
    for elem in perm:
        A, B, C, D, E = elem
        logical_expr = ((not A) and (not (B or (C and not (D and E)))))
        count += 1 if logical_expr else 0

    print('count:', count)

    # b)
    print('==========\nb) [A, B, C, D, E]')
    perm = list(product([True, False], repeat=5))
    print(f'len: {len(perm)} | {perm}')

    count = int()
    for elem in perm:
        A, B, C, D, E = elem
        logical_expr = ((A and B) and (A or C)) and (D and (not (C and E)))
        count += 1 if logical_expr else 0

    print('count:', count)

    # c)
    print('==========\nc) [A, B, C, D, E, F, G]')
    perm = list(product([True, False], repeat=7))
    print(f'len: {len(perm)} | {perm}')

    count = int()
    for elem in perm:
        A, B, C, D, E, F, G = elem
        logical_expr = (not (A or (B and (C or not (D and (not (E or (F or G))))))))
        count += 1 if logical_expr else 0

    print('count:', count)

    # d)
    print('==========\nd) [A, B, C, D, E, F, G, H]')
    perm = list(product([True, False], repeat=8))
    print(f'len: {len(perm)} | {perm}')

    count = int()
    for elem in perm:
        A, B, C, D, E, F, G, H = elem
        logical_expr = ((A and (not (B or (C and D)))) or (E and (F or (not (C and (G or H))))))
        count += 1 if logical_expr else 0

    print('count:', count)

    # e)
    print('==========\ne) [A, B, C, D, E, F, H, I, J]')
    perm = list(product([True, False], repeat=9))
    print(f'len: {len(perm)} | {perm}')

    count = int()
    for elem in perm:
        A, B, C, D, E, F, H, I, J = elem
        logical_expr = (((A and B) or (not (C or D)) and (E or (not (F and (H or (I and J)))))))
        count += 1 if logical_expr else 0

    print('count:', count)



if __name__ == '__main__':
    main()
