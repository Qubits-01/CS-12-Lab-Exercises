def main():
    secret_agent = [(2.23, 0.48)]
    guests = [
        (6.57, 8.86),
        (1.55, 5.40),
        (1.33, 1.72),
        (0.07, 3.73),
        (6.24, 8.72)
    ]

    guests_1 = [
        (4.23, 4.48),
        (6.23, 2.48),
        (6.57, 8.86),
        (6.24, 8.72),
        (1.55, 5.4)
    ]

    secret_agent.sort()
    guests.sort()

    print(secret_agent)
    print(guests)

    output = infect(secret_agent, guests)
    print(output)


def infect(list_of_infected, list_of_uninfected):
    print('RECURSION')

    # Base case.
    if len(list_of_infected) >= len(list_of_uninfected):
        return sorted(list_of_uninfected)

    list_of_infected.sort()

    round_infected = list_of_infected.copy()
    round_uninfected = list_of_uninfected

    for infected in list_of_infected:
        temp_nearest = None
        temp_infected = []

        for uninfected in round_uninfected:
            distance = (infected[0] - uninfected[0]) ** 2 + (infected[1] - uninfected[1]) ** 2

            # Determine the nearest guest/s relative to an infected person.
            if temp_nearest is None:
                temp_nearest = distance
                temp_infected.append(uninfected)
            else:
                if distance < temp_nearest:
                    temp_nearest = distance
                    temp_infected = [uninfected]
                elif distance == temp_nearest:
                    temp_infected.append(uninfected)

        # Update the list of infected and uninfected.
        round_infected.extend(temp_infected)
        round_uninfected = list(set(round_uninfected) - set(temp_infected))

        print('temp_nearest', temp_nearest)
        print(round_infected)
        print(round_uninfected)

        if len(round_uninfected) == 0:
            break

    return infect(round_infected, round_uninfected)


if __name__ == '__main__':
    main()


# v1.0
# def infect(list_of_infected, list_of_uninfected):
#     list_of_infected.sort()
#     list_of_uninfected.sort()
#
#     temp_infected = []
#
#     for i in range(len(list_of_infected)):
#         temp_nearest = []
#
#         for j in range(len(list_of_uninfected)):
#             distance = (list_of_infected[i][0] - list_of_uninfected[j][0]) ** 2 \
#                        + (list_of_infected[i][1] - list_of_uninfected[j][1]) ** 2
#
#             # Identify the the nearest guest/s.
#             if len(temp_nearest) == 0:
#                 temp_nearest.append((j, distance))
#             else:
#                 if distance == temp_nearest[0][1]:
#                     temp_nearest.append((j, distance))
#                 elif distance < temp_nearest[0][1]:
#                     temp_nearest = [(j, distance)]
#
#         temp_nearest.sort(reverse=True)
#
#         # Adjust the list of infected and uninfected base on
#         # the previously identified nearest guest/s.
#         for to_be_infected in temp_nearest:
#             temp = list_of_uninfected.pop(to_be_infected[0])
#
#             temp_infected.append(temp)
#             list_of_infected.append(temp)
#
#     # Base case.
#     if len(list_of_uninfected) == 0:
#         return sorted(temp_infected)
#
#     return infect(list_of_infected, list_of_uninfected)


# v1.1
# def infect(list_of_infected, list_of_uninfected):
#     list_of_infected.sort()
#     list_of_uninfected.sort()
#
#     temp_infected = list_of_infected.copy()
#
#     for i in range(len(list_of_infected)):
#         temp_nearest = []
#
#         for j in range(len(list_of_uninfected)):
#             distance = (list_of_infected[i][0] - list_of_uninfected[j][0]) ** 2 \
#                        + (list_of_infected[i][1] - list_of_uninfected[j][1]) ** 2
#
#             # Identify the the nearest guest/s.
#             if len(temp_nearest) == 0:
#                 temp_nearest.append((j, distance))
#             else:
#                 if distance == temp_nearest[0][1]:
#                     temp_nearest.append((j, distance))
#                 elif distance < temp_nearest[0][1]:
#                     temp_nearest = [(j, distance)]
#
#         temp_nearest.sort(reverse=True)
#
#         # Adjust the list of infected and uninfected base on
#         # the previously identified nearest guest/s.
#         for to_be_infected in temp_nearest:
#             list_of_infected.append(list_of_uninfected.pop(to_be_infected[0]))
#
#     # Base case.
#     if len(list_of_uninfected) == 0:
#         last_group = sorted(list(set(list_of_infected) - set(temp_infected)))
#
#         return last_group
#
#     return infect(list_of_infected, list_of_uninfected)


# v1.3
# def infect(list_of_infected, list_of_uninfected):
#     list_of_infected.sort()
#     list_of_uninfected.sort()
#
#     temp_infected = list_of_infected.copy()
#
#     for i in range(len(list_of_infected)):
#         temp_nearest = []
#
#         for j in range(len(list_of_uninfected)):
#             distance = (list_of_infected[i][0] - list_of_uninfected[j][0]) ** 2 \
#                        + (list_of_infected[i][1] - list_of_uninfected[j][1]) ** 2
#
#             # Identify the the nearest guest/s.
#             if len(temp_nearest) == 0:
#                 temp_nearest.append((j, distance))
#             else:
#                 if distance == temp_nearest[0][1]:
#                     temp_nearest.append((j, distance))
#                 elif distance < temp_nearest[0][1]:
#                     temp_nearest = [(j, distance)]
#
#         temp_nearest.sort(reverse=True)
#
#         # Adjust the list of infected and uninfected base on
#         # the previously identified nearest guest/s.
#         for to_be_infected in temp_nearest:
#             list_of_infected.append(list_of_uninfected.pop(to_be_infected[0]))
#
#         if len(list_of_uninfected) == 0:
#             break
#
#     # Base case.
#     if len(list_of_uninfected) == 0:
#         last_group = sorted(list(set(list_of_infected) - set(temp_infected)))
#
#         return last_group
#
#     return infect(list_of_infected, list_of_uninfected)


# 1.4
# def infect(list_of_infected, list_of_uninfected):
#     # Base case.
#     if len(list_of_infected) >= len(list_of_uninfected):
#         return sorted(list_of_uninfected)
#
#     list_of_infected.sort()
#     list_of_uninfected.sort()
#
#     for i in range(len(list_of_infected)):
#         temp_nearest = []
#
#         for j in range(len(list_of_uninfected)):
#             distance = (list_of_infected[i][0] - list_of_uninfected[j][0]) ** 2 \
#                        + (list_of_infected[i][1] - list_of_uninfected[j][1]) ** 2
#
#             # Identify the the nearest guest/s.
#             if len(temp_nearest) == 0:
#                 temp_nearest.append((j, distance))
#             else:
#                 if distance == temp_nearest[0][1]:
#                     temp_nearest.append((j, distance))
#                 elif distance < temp_nearest[0][1]:
#                     temp_nearest = [(j, distance)]
#
#         temp_nearest.sort(reverse=True)
#
#         # Adjust the list of infected and uninfected base on
#         # the previously identified nearest guest/s.
#         for to_be_infected in temp_nearest:
#             list_of_infected.append(list_of_uninfected.pop(to_be_infected[0]))
#
#         if len(list_of_uninfected) == 0:
#             break
#
#     return infect(list_of_infected, list_of_uninfected)


# v1.5
# def infect(list_of_infected, list_of_uninfected):
#     if len(list_of_infected) >= len(list_of_uninfected):
#         return sorted(list_of_uninfected)
#
#     list_of_infected.sort()
#     list_of_uninfected.sort()
#
#     for i in range(len(list_of_infected)):
#         temp_nearest = []
#
#         for j in range(len(list_of_uninfected)):
#             if len(temp_nearest) != 0:
#                 if (abs(list_of_uninfected[j][0] - list_of_infected[i][0]) > abs(list_of_uninfected[temp_nearest[0][0]][0] - list_of_infected[i][0])) \
#                         and (abs(list_of_uninfected[j][1] - list_of_infected[i][1]) > abs(list_of_uninfected[temp_nearest[0][0]][1] - list_of_infected[i][1])):
#                     continue
#
#             distance = (list_of_infected[i][0] - list_of_uninfected[j][0]) ** 2 \
#                        + (list_of_infected[i][1] - list_of_uninfected[j][1]) ** 2
#
#             # Identify the nearest guest/s.
#             if len(temp_nearest) == 0:
#                 temp_nearest.append((j, distance))
#             else:
#                 if distance == temp_nearest[0][1]:
#                     temp_nearest.append((j, distance))
#                 elif distance < temp_nearest[0][1]:
#                     temp_nearest = [(j, distance)]
#
#         temp_nearest.sort(reverse=True)
#
#         # Adjust the list of infected and uninfected base on
#         # the previously identified nearest guest/s.
#         for to_be_infected in temp_nearest:
#             list_of_infected.append(list_of_uninfected.pop(to_be_infected[0]))
#
#         if len(list_of_uninfected) == 0:
#             break
#
#     return infect(list_of_infected, list_of_uninfected)


# v.2.1
# def infect(list_of_infected, list_of_uninfected):
#     # Base case.
#     if len(list_of_infected) >= len(list_of_uninfected):
#         return sorted(list_of_uninfected)
#
#     list_of_infected.sort()
#
#     round_infected = list_of_infected.copy()
#     round_uninfected = list_of_uninfected
#
#     for infected in list_of_infected:
#         temp_nearest = None
#         temp_infected = []
#
#         for uninfected in round_uninfected:
#             distance = (infected[0] - uninfected[0]) ** 2 + (infected[1] - uninfected[1]) ** 2
#
#             # Determine the nearest guest/s relative to an infected person.
#             if temp_nearest is None:
#                 temp_nearest = distance
#                 temp_infected.append(uninfected)
#             else:
#                 if distance < temp_nearest:
#                     temp_nearest = distance
#                     temp_infected = [uninfected]
#                 elif distance == temp_nearest:
#                     temp_infected.append(uninfected)
#
#         # Update the list of infected and uninfected.
#         round_infected.extend(temp_infected)
#         round_uninfected = list(set(round_uninfected) - set(temp_infected))
#
#         if len(round_uninfected) == 0:
#             break
#
#     return infect(round_infected, round_uninfected)


