from itertools import combinations, \
    permutations


def main():
    n_test_cases = 2
    members_1 = '30 30 60 90 100'
    members_2 = '40 50 60 90 100 100'

    members_1 = [int(member) for member in members_2.split()]
    print(members_1)

    possible_sets = list(combinations(members_1, 5))
    print(possible_sets)

    n_qualified_team = 0
    for t_members in possible_sets:
        # Check if the scores of the members are unique.
        if len(set(t_members)) != 5:
            continue

        n_passing = 0
        avg_score = 0

        for t_member in t_members:
            if t_member >= 60:
                n_passing += 1

            avg_score += t_member

        # Check if there are at least 3 members who have a score >= 60.
        if n_passing >= 3:
            avg_score = avg_score / 5
        else:
            continue

        # Check if the average score of the members >= 65.
        if avg_score >= 65:
            n_permutation = len(list(permutations(t_members, 5)))

            n_qualified_team += n_permutation

    print(n_qualified_team)


if __name__ == '__main__':
    main()


# from itertools import combinations, \
#     permutations
#
#
# def main():
#     n_test_cases = int(input())
#
#     for _ in range(n_test_cases):
#         members_1 = [int(member) for member in input().split()]
#
#         possible_sets = list(combinations(members_1, 5))
#         n_qualified_team = 0
#
#         for t_members in possible_sets:
#             # Check if the scores of the members are unique.
#             if len(set(t_members)) != 5:
#                 continue
#
#             n_passing = 0
#             avg_score = 0
#
#             for t_member in t_members:
#                 if t_member >= 60:
#                     n_passing += 1
#
#                 avg_score += t_member
#
#             # Check if there are at least 3 members who have a score >= 60.
#             if n_passing >= 3:
#                 avg_score = avg_score / 5
#             else:
#                 continue
#
#             # Check if the average score of the members >= 65.
#             if avg_score >= 65:
#                 n_permutation = len(list(permutations(t_members, 5)))
#
#                 n_qualified_team += n_permutation
#
#         print(n_qualified_team)
#
#
# if __name__ == '__main__':
#     main()
