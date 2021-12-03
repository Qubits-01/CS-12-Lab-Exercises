def count_food_combinations(pricelist, minimum_meal_num, budget, meals_so_far):
    if len(pricelist[-1]) == 2:
        pricelist.append([0, [], []])
        return count_food_combinations(pricelist, minimum_meal_num, budget, meals_so_far)

    temp_price = pricelist[-1]

    if budget == 0:
        if len(temp_price[2]) >= minimum_meal_num:
            temp_price[1].append(list(temp_price[2]))

        return

    for i in range(temp_price[0], len(pricelist) - 1):
        prices = pricelist[i]

        if (budget - prices[1]) >= 0:
            # Finding meal option/s that might contribute to the budget.
            temp_price[2].append(prices[1])
            pricelist[:len(pricelist) - 1].append(temp_price)
            count_food_combinations(pricelist, minimum_meal_num, budget - prices[1], meals_so_far)

            # Backtracking: removing invalid meal option/s.
            temp_price[2].remove(prices[1])

    return temp_price[1]


ans = count_food_combinations([("Silog", 10), ("Apple", 20), ("qwe", 20)], 5, 70, 0)
print(len(ans), ans)
