def combinationSum(pricelist, minimum_meal_num, budget):
    ans = []
    temp = []

    # first do hashing nothing but set{}
    # since set does not always sort
    # removing the duplicates using Set and
    # Sorting the List
    # pricelist.sort()
    findNumbers(ans, pricelist, minimum_meal_num, temp, budget, 0)
    return ans


def findNumbers(ans, pricelist, minimum_meal_num, temp, budget, index):
    if budget == 0:
        # Adding deep copy of list to ans
        if len(temp) >= minimum_meal_num:
            ans.append(list(temp))

        return

    # Iterate from index to len(arr) - 1
    for i in range(index, len(pricelist)):
        prices = pricelist[i]

        # Checking that the budget does not become negative
        if (budget - prices[1]) >= 0:
            # Adding element which can contribute to the budget.
            temp.append(prices[1])
            findNumbers(ans, pricelist, minimum_meal_num, temp, budget - prices[1], i)

            # removing element from list (backtracking)
            temp.remove(prices[1])


ans = combinationSum([("Silog", 10), ("Apple", 20)], 5, 70)
print(ans)
