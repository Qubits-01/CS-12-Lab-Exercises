def main():
    # Sorted list.
    li_a = [1, 3, 4, 5, 32, 45, 56, 70]

    # Unsorted list.
    # Rotated 2 steps to the left relative to li_a.
    li_b = [4, 5, 32, 45, 56, 70, 1, 3]

    print('No. 2')
    index = binary_search(li_b, 5)
    print(f'Index of element 5 in {li_b} :  {index}  [Correct]')

    index = binary_search(li_b, 45)
    print(f'Index of element 45 in {li_b} :  {index}  [Correct]')

    print('\nNo. 3')
    index = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
    print(f'[BS] Index of element 5 in {li_b} :  {index}  [steps: {steps}]')

    index = linear_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
    print(f'[LS] Index of element 5 in {li_b} :  {index}  [steps: {steps}]')



# From CS12 Lecture Note.
steps = 0
def binary_search(li, num):
    global steps
    steps += 1

    if not li:
        return -1

    mid = len(li) // 2
    res = -1

    if num == li[mid]:
        res = mid
    elif num < li[mid]:
        return binary_search(li[:mid], num)
    else:  # num > li[mid]
        res = binary_search(li[mid + 1:], num)
        if res != -1:
            res += mid + 1

    return res


def linear_search(li, num):
    global steps
    steps = 0

    for i in range(len(li)):
        steps += 1
        if num == li[i]:
            return i

    return -1


if __name__ == '__main__':
    main()
