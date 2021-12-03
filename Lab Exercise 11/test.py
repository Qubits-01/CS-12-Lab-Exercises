def count_food_combinations(prices, min_meals, budget, calc_meals):
    # Initialize needed metadata.
    if len(prices[-1]) == 2:
        prices.append([0, 0, []])
        return count_food_combinations(prices, min_meals, budget, calc_meals)
    else:
        return len(solve(prices, min_meals, budget, calc_meals))


def solve(prices, min_meals, budget, calc_meals):
    temp_prices = prices[-1]

    # Base case/s.
    if temp_prices[1] == budget:
        return tuple(temp_prices[2])
    # Backtrack.
    elif temp_prices[1] > budget:
        return None
    else:
        meal_combinations = []
        n = len(prices) - 1

        for price in prices[:n]:
            temp_price = prices[:n]
            temp_price.append([temp_prices[0], temp_prices[1] + price[1], temp_prices[2] + [price[1]]])

            mc = solve(temp_price, min_meals, budget, calc_meals)

            if (type(mc) is tuple) and len(mc) >= min_meals:
                temp_prices[0] += 1
                calc_meals += 1
                meal_combinations.append(mc)

            if type(mc) is list:
                meal_combinations.extend(mc)

        return meal_combinations


OTHER_RECURSIVE_FUNCTIONS = ['solve']


a = count_food_combinations([("Silog", 10), ("Apple", 20), ('wewe', 20)], 5, 70, 0)
print(a)
