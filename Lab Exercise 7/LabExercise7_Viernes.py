def main():
    cumulative_exp = 0
    base_exp_list = [1650, 100]
    index = 0

    print(solve_level(cumulative_exp, base_exp_list, index))


# def solve_level(cumulative_exp, base_exp_list, index):
#     size = len(base_exp_list)
#
#     if size == 1:
#         return base_exp_list[0]
#
#     index += 1
#
#     return base_exp_list[-1] + solve_level(cumulative_exp, base_exp_list[:size-1], index)


# def solve_level(cumulative_exp, base_exp_list, index):
#     final_level = solve_final_level(cumulative_exp, base_exp_list, index)
#     final_cumulative_exp = solve_final_cumulative_exp(base_exp_list)
#
#     index += 1
#
#     return final_level, final_cumulative_exp


def solve_level(cumulative_exp, base_exp_list, index):
    temp_lvl = cumulative_exp // 15
    cumulative_exp = cumulative_exp + (base_exp_list[index] * max(temp_lvl//10, 1))

    # Base case.
    if index == (len(base_exp_list) - 1):
        return cumulative_exp // 15, cumulative_exp

    index += 1

    return solve_level(cumulative_exp, base_exp_list, index)


# def solve_final_cumulative_exp(base_exp_list):
#     size = len(base_exp_list)
#
#     # Base case.
#     if size == 1:
#         return base_exp_list[0]
#
#     # Recursive step.
#     return base_exp_list[-1] + solve_final_cumulative_exp(base_exp_list[:size-1])


if __name__ == '__main__':
    main()
