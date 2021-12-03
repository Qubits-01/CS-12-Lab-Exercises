def main():
    solved = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    unsolved = [
        [1, 2, 3],
        [4, 5, 0],
        [7, 8, 6]
    ]

    output = solve_puzzle(solved, unsolved, [], [])
    print(output)


def solve_puzzle(solved, unsolved, prev_states, directions):
    pass


if __name__ == '__main__':
    main()
