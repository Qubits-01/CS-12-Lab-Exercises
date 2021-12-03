from copy import deepcopy

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
    print('output', output)


def solve_puzzle(solved, unsolved, prev_states, directions):
    # import sys
    # sys.setrecursionlimit(50000)

    # Initialize.
    if len(directions) == 0:
        prev_states.append(unsolved.copy())
        return solve_puzzle(solved, unsolved, prev_states, [['']])
    else:
        # Base case.
        if len(prev_states) == 0:
            return [], 0

        curr_unsolved = prev_states.pop(0)
        curr_directions = directions.pop(0)
        print(curr_unsolved)
        print(len(curr_directions)-1, curr_directions)

        # Base case/s.
        if (len(curr_directions) - 1) > 8:
            return [], 0

        if solved == curr_unsolved:
            print('SOLVED!', curr_unsolved)
            return curr_directions[1:], len(curr_directions) - 1

        def deep_copy(lst):
            lst_copy = []
            for row in lst:
                lst_copy.append(row.copy())

            return lst_copy

        zero_xy = None
        for row in curr_unsolved:
            if 0 in row:
                zero_xy = (row.index(0), curr_unsolved.index(row))
                break

        # zero up
        if (zero_xy[1] != 0) and (curr_directions[-1] != 'up'):
            # print('up', curr_unsolved)

            # Swap the two elements.
            unsolved_copy = deep_copy(curr_unsolved)
            swap_elem = unsolved_copy[zero_xy[1] - 1][zero_xy[0]]
            unsolved_copy[zero_xy[1] - 1][zero_xy[0]] = 0
            unsolved_copy[zero_xy[1]][zero_xy[0]] = swap_elem
            prev_states.append(unsolved_copy)

            # Update direction/s.
            directions_copy = curr_directions.copy()
            directions_copy.append('down')
            directions.append(directions_copy)

        # zero down
        if (zero_xy[1] != 2) and (curr_directions[-1] != 'down'):
            # print('down', curr_unsolved)

            # Swap the two elements.
            unsolved_copy = deep_copy(curr_unsolved)
            swap_elem = unsolved_copy[zero_xy[1] + 1][zero_xy[0]]
            unsolved_copy[zero_xy[1] + 1][zero_xy[0]] = 0
            unsolved_copy[zero_xy[1]][zero_xy[0]] = swap_elem
            prev_states.append(unsolved_copy)

            # Update direction/s.
            directions_copy = curr_directions.copy()
            directions_copy.append('up')
            directions.append(directions_copy)

        # zero left
        if (zero_xy[0] != 0) and (curr_directions[-1] != 'left'):
            # print('left', curr_unsolved)

            # Swap the two elements.
            unsolved_copy = deep_copy(curr_unsolved)
            swap_elem = unsolved_copy[zero_xy[1]][zero_xy[0] - 1]
            unsolved_copy[zero_xy[1]][zero_xy[0] - 1] = 0
            unsolved_copy[zero_xy[1]][zero_xy[0]] = swap_elem
            prev_states.append(unsolved_copy)

            # Update direction/s.
            directions_copy = curr_directions.copy()
            directions_copy.append('right')
            directions.append(directions_copy)

        # zero right
        if (zero_xy[0] != 2) and (curr_directions[-1] != 'right'):
            # print('right', curr_unsolved)

            # Swap the two elements.
            unsolved_copy = deep_copy(curr_unsolved)
            swap_elem = unsolved_copy[zero_xy[1]][zero_xy[0] + 1]
            unsolved_copy[zero_xy[1]][zero_xy[0] + 1] = 0
            unsolved_copy[zero_xy[1]][zero_xy[0]] = swap_elem
            prev_states.append(unsolved_copy)

            # Update direction/s.
            directions_copy = curr_directions.copy()
            directions_copy.append('left')
            directions.append(directions_copy)

        return solve_puzzle(solved, curr_unsolved, prev_states, directions)


if __name__ == '__main__':
    main()


# def solve_puzzle(solved, unsolved, prev_states, directions):
#     # Initialize the starting point for the Breadth-First Search.
#     if len(directions) == 0:
#         prev_states.append(unsolved.copy())
#         return solve_puzzle(solved, unsolved, prev_states, [['']])
#     else:
#         # Base case.
#         if len(prev_states) == 0:
#             return [], 0
#
#         curr_unsolved = prev_states.pop(0)
#         curr_directions = directions.pop(0)
#
#         # Base case/s.
#         # Lowering it to 8 (from 15) because of the recursion depth limit.
#         # As it turns out, 8 will do just fine.
#         # Thus, I can also remove the code that modifies
#         # the runtime's recursion limit (that is well adjusted
#         # to length 15).
#         if (len(curr_directions) - 1) > 8:
#             return [], 0
#
#         if solved == curr_unsolved:
#             return curr_directions[1:], len(curr_directions) - 1
#
#         def deep_copy(lst):
#             lst_copy = []
#             for row in lst:
#                 lst_copy.append(row.copy())
#
#             return lst_copy
#
#         zero_xy = None
#         for row in curr_unsolved:
#             if 0 in row:
#                 zero_xy = (row.index(0), curr_unsolved.index(row))
#                 break
#
#         # import sys
#         # sys.setrecursionlimit(32500)
#
#         # zero up
#         if (zero_xy[1] != 0) and (curr_directions[-1] != 'up'):
#             # Swap the two elements.
#             unsolved_copy = deep_copy(curr_unsolved)
#             swap_elem = unsolved_copy[zero_xy[1] - 1][zero_xy[0]]
#             unsolved_copy[zero_xy[1] - 1][zero_xy[0]] = 0
#             unsolved_copy[zero_xy[1]][zero_xy[0]] = swap_elem
#             prev_states.append(unsolved_copy)
#
#             # Update direction/s.
#             directions_copy = curr_directions.copy()
#             directions_copy.append('down')
#             directions.append(directions_copy)
#
#         # zero down
#         if (zero_xy[1] != 2) and (curr_directions[-1] != 'down'):
#             # Swap the two elements.
#             unsolved_copy = deep_copy(curr_unsolved)
#             swap_elem = unsolved_copy[zero_xy[1] + 1][zero_xy[0]]
#             unsolved_copy[zero_xy[1] + 1][zero_xy[0]] = 0
#             unsolved_copy[zero_xy[1]][zero_xy[0]] = swap_elem
#             prev_states.append(unsolved_copy)
#
#             # Update direction/s.
#             directions_copy = curr_directions.copy()
#             directions_copy.append('up')
#             directions.append(directions_copy)
#
#         # zero left
#         if (zero_xy[0] != 0) and (curr_directions[-1] != 'left'):
#             # Swap the two elements.
#             unsolved_copy = deep_copy(curr_unsolved)
#             swap_elem = unsolved_copy[zero_xy[1]][zero_xy[0] - 1]
#             unsolved_copy[zero_xy[1]][zero_xy[0] - 1] = 0
#             unsolved_copy[zero_xy[1]][zero_xy[0]] = swap_elem
#             prev_states.append(unsolved_copy)
#
#             # Update direction/s.
#             directions_copy = curr_directions.copy()
#             directions_copy.append('right')
#             directions.append(directions_copy)
#
#         # zero right
#         if (zero_xy[0] != 2) and (curr_directions[-1] != 'right'):
#             # Swap the two elements.
#             unsolved_copy = deep_copy(curr_unsolved)
#             swap_elem = unsolved_copy[zero_xy[1]][zero_xy[0] + 1]
#             unsolved_copy[zero_xy[1]][zero_xy[0] + 1] = 0
#             unsolved_copy[zero_xy[1]][zero_xy[0]] = swap_elem
#             prev_states.append(unsolved_copy)
#
#             # Update direction/s.
#             directions_copy = curr_directions.copy()
#             directions_copy.append('left')
#             directions.append(directions_copy)
#
#         return solve_puzzle(solved, curr_unsolved, prev_states, directions)
