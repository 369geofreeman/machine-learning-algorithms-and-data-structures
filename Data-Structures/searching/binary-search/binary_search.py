def binary_search(input_array, value):
    """Your code goes here."""
    l, r = 0, len(input_array)

    while l <= r:
        mid = l+(r-l)//2

        if input_array[mid] == value:
            return mid

        if input_array[mid] > value:
            r = mid - 1
        else:
            l = mid + 1

    return -1


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15

print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
