def main():
    max_weight = 1000
    games_info = (
        ("TheLegendofZelda", 200, 8),
        ("Pokemon ", 800, 10),
        ("GhostofTsushima", 300, 7.5),
        ("FinalFantasyXIV", 600, 9),
        ("TheLastOfUs", 100, 10),
        ("MarioKart", 500, 9)
    )

    total_ms, selected_games = knapsack(games_info, max_weight)
    print(total_ms / len(selected_games))
    print(sorted(selected_games))


def knapsack(games_info, max_weight):
    table = [[0 for w in range(max_weight+1)] for j in range(len(games_info)+1)]

    for game in range(1, len(games_info)+1):
        curr_weight, curr_val = games_info[game-1][1:]
        for weight in range(1, max_weight+1):
            if curr_weight > weight:
                table[game][weight] = table[game-1][weight]
            else:
                table[game][weight] = max(table[game-1][weight], table[game-1][weight-curr_weight] + curr_val)

    total_ms, selected_games = 0, []
    for i in range(len(games_info), 0, -1):
        if table[i][max_weight] != table[i-1][max_weight]:
            total_ms += games_info[i-1][2]
            selected_games.append(games_info[i-1][0])
            max_weight -= games_info[i-1][1]

    return total_ms, selected_games


if __name__ == '__main__':
    main()


# def main():
#     max_weight = int(input())
#     n = int(input())  # No. of game/s.
#
#     games_info = []
#     for _ in range(n):
#         temp = input().split()
#         games_info.append(tuple([temp[0], int(temp[2]), float(temp[1])]))
#     games_info = tuple(games_info)
#
#     total_ms, selected_games = knapsack(games_info, max_weight)
#     print(total_ms / len(selected_games))
#     print(sorted(selected_games))
#
#
# def knapsack(games_info, max_weight):
#     table = [[0 for w in range(max_weight + 1)] for j in range(len(games_info) + 1)]
#
#     for game in range(1, len(games_info) + 1):
#         curr_weight, curr_val = games_info[game - 1][1:]
#         for weight in range(1, max_weight + 1):
#             if curr_weight > weight:
#                 table[game][weight] = table[game - 1][weight]
#             else:
#                 table[game][weight] = max(table[game - 1][weight], table[game - 1][weight - curr_weight] + curr_val)
#
#     total_ms, selected_games = 0, []
#     for i in range(len(games_info), 0, -1):
#         if table[i][max_weight] != table[i - 1][max_weight]:
#             total_ms += games_info[i - 1][2]
#             selected_games.append(games_info[i - 1][0])
#             max_weight -= games_info[i - 1][1]
#
#     return total_ms, selected_games
#
#
# if __name__ == '__main__':
#     main()
