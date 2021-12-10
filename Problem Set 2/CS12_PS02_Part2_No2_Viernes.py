def main():
    A, L = 3, 2
    valid_sequences = solve(A, L)

    print('Ex) A=3, L=2')
    print(len(valid_sequences))
    print(valid_sequences)

    A, L = 3, 3
    valid_sequences = solve(A, L)

    print('\na) A=3, L=3')
    print(len(valid_sequences))
    print(valid_sequences)

    A, L = 5, 2
    valid_sequences = solve(A, L)

    print('\nb) A=5, L=2')
    print(len(valid_sequences))
    print(valid_sequences)

    A, L = 6, 4
    valid_sequences = solve(A, L)

    print('\nc) A=6, L=4')
    print(len(valid_sequences))
    print(valid_sequences)

    A, L = 7, 5
    valid_sequences = solve(A, L)

    print('\nd) A=7, L=5')
    print(len(valid_sequences))
    # print(valid_sequences)

    A, L = 7, 6
    valid_sequences = solve(A, L)

    print('\ne) A=7, L=6')
    print(len(valid_sequences))
    # print(valid_sequences)


def solve(A, L, curr_sequence=''):
    count_A, count_L = int(), int()
    for char in curr_sequence:
        if 'A' == char:
            count_A += 1
        else:
            count_L += 1

    if (count_A + (count_L // L)) == A:
        return [curr_sequence]

    return solve(A, L, curr_sequence+'A') + solve(A, L, curr_sequence+'L')


if __name__ == '__main__':
    main()
