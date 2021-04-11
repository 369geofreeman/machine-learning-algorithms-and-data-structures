# Quick Sort
# ---


# Quick sort is a divide and conquer algo that is usually written recursively.
# It merges first and then splits the list
# We take one element and sort it, then use use that as pivot
# Recursevely we do that again from left to right. this is called partitioning
# There are two ways to partition the list

# Average time complexity O(n Log n)
# Worst case of O(n²)


def swap(a, b, arr):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]


def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1

        while elements[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)

    return end


def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi - 1)  # left partition
        quick_sort(elements, pi+1, end)  # Right partition


if __name__ == "__main__":
    elements = [11, 9, 29, 7, 2, 15, 28]
    quick_sort(elements, 0, len(elements) - 1)
    print(elements)



