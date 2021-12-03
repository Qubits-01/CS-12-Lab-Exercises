def main():
    calc_meals = 0

    prices1 = [("Silog", 10), ("Apple", 20)]
    min_meals1 = 5
    budget1 = 70

    print(count_food_combinations(prices1, min_meals1, budget1, calc_meals))


def count_food_combinations(prices, min_meals, budget, calc_meals):

    if calc_meals == 0:
        calc_meals = [0, []]

    # Base case/s.
    if calc_meals[0] == budget:
        return tuple(calc_meals[1])
    # Backtrack.
    elif calc_meals[0] > budget:
        return None
    else:
        meal_combinations = []

        for price in prices:
            cm_metadata = [calc_meals[0] + price[1], calc_meals[1] + [price[1]]]

            mc = count_food_combinations(prices, min_meals, budget, cm_metadata)

            if (type(mc) is tuple) and len(mc) >= min_meals:
                meal_combinations.append(mc)

            if type(mc) is list:
                meal_combinations.extend(mc)

        return meal_combinations


if __name__ == '__main__':
    main()
