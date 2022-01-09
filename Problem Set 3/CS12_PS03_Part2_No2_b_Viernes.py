def main():
    ans = pascal_triangle(4, 4)
    print(ans)


def pascal_triangle(row, col):
    C = [0] * (row + 1)
    for r in range(row + 1):
        C[r] = [0] * (col + 1)
    print(C)

    for i in range(row + 1):
        for j in range(col + 1):
            if j == 0 or i == j:
                C[i][j] = 1
            else:
                C[i][j] = C[i - 1][j] + C[i - 1][j - 1]

        print(C)

    return C[row][col]


if __name__ == '__main__':
    main()
