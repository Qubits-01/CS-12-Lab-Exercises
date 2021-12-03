def main():
    ns = [
        [20.45, 88.76],
        [35.35, 80.16],
        [7.98, 49.30],
        [55.44, 4.73],
        [89.48, 53.33],
        [76.77, 93.76],
        [54.33, 13.16],
        [46.93, 40.00],
        [37.28, 87.48],
        [29.70, 57.31]
    ]
    ms = [
        [15.58, 52.26],
        [86.49, 13.15],
        [97.57, 0.06]
    ]

    biggest_r2 = []

    l = 0
    for n1 in ns:
        temp_biggest_r2 = []

        for n2 in ns:
            if n1 == n2:
                continue

            temp_biggest_r2.append((get_r2(n1, n2)))
            temp_biggest_r2 = [max(temp_biggest_r2)]

        temp = [n1]
        temp.append(temp_biggest_r2)
        biggest_r2.append(temp)

    print('biggest_r2', biggest_r2)

    possible_ps = []

    for c in biggest_r2:
        smallest_mr2 = []

        for m in ms:
            print('1', c[0], m, get_r2(c[0], m), c[1][0])
            smallest_mr2.append(get_r2(c[0], m))
            smallest_mr2 = [min(smallest_mr2)]

        if smallest_mr2[0] <= c[1][0]:
            continue
        else:
            possible_ps.append(c[0])


    max_r2 = []
    for p1 in possible_ps:
        for p2 in ns:
            max_r2.append(get_r2(p1, p2))
            max_r2 = [max(max_r2)]

    print(max_r2)
    # print(max_r2[0] ** (1 / 2))


def get_r2(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


if __name__ == '__main__':
    main()
