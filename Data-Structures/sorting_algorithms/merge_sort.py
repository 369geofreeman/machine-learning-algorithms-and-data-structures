# Merge Sort
# ---


# Merge sort is an instance of a divide and conquer algorithm. The basic premise
# is we divide a problem into two pieces. Each of the the two pieces are easier
# to solve rather than attempting the entire thing, because they are smaller.


def mergeTwoSortedLists(a, b, arr):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] < b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1

    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1

    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1


def merge_sort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    mergeTwoSortedLists(left, right, arr)


if __name__ == '__main__':
    test_cases = [
        [],
        [3],
        [9, 8, 7, 2],
        [1, 2, 3, 4, 5],
        [5, 8, 12, 56, 7, 9, 45, 51, 100]
        ]

    for arr in test_cases:
        merge_sort(arr)
        print(arr)


