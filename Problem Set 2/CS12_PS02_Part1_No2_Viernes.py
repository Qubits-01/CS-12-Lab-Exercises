def main():
    # Sorted list.
    li_a = [1, 3, 4, 5, 32, 45, 56, 70]

    # Unsorted list.
    # Rotated 2 steps to the left relative to li_a.
    li_b = [4, 5, 32, 45, 56, 70, 1, 3]

    index = binary_search(li_b, 5)
    print(f'Index of element 5 in {li_b} :  {index}  [Correct]')

    index = binary_search(li_b, 45)
    print(f'Index of element 45 in {li_b} :  {index}  [Correct]')


# From CS12 Lecture Note.
def binary_search(li, num):
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


if __name__ == '__main__':
    main()
