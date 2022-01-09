def main():
    ans = factorial(8)
    print(ans)


def factorial(n):
    memo = [1]
    for i in range(1, n+1):
        memo.append(memo[i-1] * i)
        print(memo)

    return memo[-1]


if __name__ == '__main__':
    main()
