def main():
    ints = [6, 8, 9, 10, 18, 76, 171, 342]
    primes_of_ints = {}

    for n in ints:
        primes_of_ints[n] = prime_factors(n)

    print(primes_of_ints)

    ctr = 0

    adjacency = {}

    for i in ints:
        ctr += 1

        for j in ints[ctr:]:
            intersection = primes_of_ints[i].intersection(primes_of_ints[j])

            if len(intersection) >= 2:
                if i in adjacency:
                    adjacency[i].append((j, sum(intersection)))
                else:
                    adjacency[i] = [(j, sum(intersection))]

                if j in adjacency:
                    adjacency[j].append((i, sum(intersection)))
                else:
                    adjacency[j] = [(i, sum(intersection))]

    print(adjacency)

    for n in ints:
        if n in adjacency:
            print(f'{n} : {sorted(adjacency[n], key=lambda adjacency_datum: adjacency_datum[0])}')
        else:
            print(f'{n} : {[]}')


def prime_factors(n):
    factors = set()

    # When n is still even.
    while n % 2 == 0:
        factors.add(2)
        n /= 2

    # When n is now odd.
    for i in range(3, int(n ** (1 / 2)) + 1, 2):
        while n % i == 0:
            factors.add(i)
            n /= i

    if n > 2:
        factors.add(int(n))

    return factors


if __name__ == '__main__':
    main()


# def main():
#     ints = [int(n) for n in input().split()]
#     primes_of_ints = {}
#
#     for n in ints:
#         primes_of_ints[n] = prime_factors(n)
#
#     ctr = 0
#     adjacency = {}
#
#     for i in ints:
#         ctr += 1
#
#         for j in ints[ctr:]:
#             intersection = primes_of_ints[i].intersection(primes_of_ints[j])
#
#             if len(intersection) >= 2:
#                 if i in adjacency:
#                     adjacency[i].append((j, sum(intersection)))
#                 else:
#                     adjacency[i] = [(j, sum(intersection))]
#
#                 if j in adjacency:
#                     adjacency[j].append((i, sum(intersection)))
#                 else:
#                     adjacency[j] = [(i, sum(intersection))]
#
#     for n in ints:
#         if n in adjacency:
#             print(f'{n} : {adjacency[n]}')
#         else:
#             print(f'{n} : {[]}')
#
#
# def prime_factors(n):
#     factors = set()
#
#     # When n is still even.
#     while n % 2 == 0:
#         factors.add(2)
#         n /= 2
#
#     # When n is now odd.
#     for i in range(3, int(n ** (1 / 2)) + 1, 2):
#         while n % i == 0:
#             factors.add(i)
#             n /= i
#
#     if n > 2:
#         factors.add(int(n))
#
#     return factors
#
#
# if __name__ == '__main__':
#     main()
