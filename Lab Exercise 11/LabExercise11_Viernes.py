def main():
    price_list = [("Silog", 10), ("Apple", 20)]
    minimum_meal_num = 5
    budget = 70

    possible_meal_permutation = count_food_combinations(price_list, minimum_meal_num, budget, 0)
    print(possible_meal_permutation)


def count_food_combinations(price_list, minimum_meal_num, budget, meals_so_far):
    # Initialize
    if type(price_list[0]) is not int:
        price_list.sort(key=lambda meal_price: meal_price[1])
        min_price = price_list[0][1]
        price_list.insert(0, min_price)

        return count_food_combinations(price_list, minimum_meal_num, budget, meals_so_far)
    else:
        # Base cases (if the meal combination/s so far satisfies the
        # given requirements).
        if price_list[0] > budget:
            if meals_so_far >= minimum_meal_num:
                return True
            else:
                return 0

        possible_meal_combinations = 0
        for meal_price in price_list[1:]:
            if budget >= meal_price[1]:
                temp_meal_count = count_food_combinations(price_list, minimum_meal_num,
                                                          budget-meal_price[1], meals_so_far + 1)

                if temp_meal_count is True:
                    possible_meal_combinations += 1
                else:
                    possible_meal_combinations += temp_meal_count

        return possible_meal_combinations


if __name__ == '__main__':
    main()


# def count_food_combinations(price_list, minimum_meal_num, budget, meals_so_far):
#     # Initialize
#     if type(price_list[0]) is not int:
#         price_list.sort(key=lambda meal_price: meal_price[1])
#         min_price = price_list[0][1]
#         price_list.insert(0, min_price)
#
#         return count_food_combinations(price_list, minimum_meal_num, budget, meals_so_far)
#     else:
#         # Base cases (if the meal combination/s so far satisfies the
#         # given requirements).
#         if price_list[0] > budget:
#             if meals_so_far >= minimum_meal_num:
#                 return True
#             else:
#                 return 0
#
#         possible_meal_combinations = 0
#         for meal_price in price_list[1:]:
#             if budget >= meal_price[1]:
#                 temp_meal_count = count_food_combinations(price_list, minimum_meal_num,
#                                                           budget-meal_price[1], meals_so_far + 1)
#
#                 if temp_meal_count is True:
#                     possible_meal_combinations += 1
#                 else:
#                     possible_meal_combinations += temp_meal_count
#
#         return possible_meal_combinations
