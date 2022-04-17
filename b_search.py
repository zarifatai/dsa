def binary_search(lst, item):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = lst[mid]

        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        elif guess > item:
            high = mid - 1
    return None

print(binary_search([1,2,3,4,5,6,7,8,9], 7))

