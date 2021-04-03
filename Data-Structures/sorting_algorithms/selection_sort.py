# Selection Sort
# ---

# The algorithm begins by finding the smallest value to place in the first
# position in the list. It does this by doing a linear search through
# the list and along the way remembering the index of the smallest item it finds.
# The algorithm uses the guess and check pattern by forst guessing that the smallest
# item is the first item in the list and then checking the subsequent items
# to see if it made an incorrect guess. This part of the algorithm is the selection
# part.


def selSort(A):
    # Traverse through all array elements
    for i in range(len(A)):

        # Find the minimum element in remaining 
        # unsorted array
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j

        # Swap the found minimum element with 
        # the first element        
        A[i], A[min_idx] = A[min_idx], A[i]

    return A


def main():
    lst = [5, 8, 2, 6, 9, 1, 0, 7]
    lst = selSort(lst)
    print(lst, 'hi')


if __name__ == "__main__":
    main()


