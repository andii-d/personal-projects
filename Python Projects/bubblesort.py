def bubbleSort(array):
    # n is the pass number
    n = len(array)

    # Sort for the pass number amount of time
    for i in range(n):
        # For each item in the array, iterate until fully sorted
        # n-i-1 = len(array) - end position - 1
        # This is to restart the index and sort from the left.
        for k in range(0, n-i-1):
            # If the first value is bigger than the next
            if array[k] > array[k+1]:
                # Swap the values
                array[k], array[k+1] = array[k+1], array[k]
            # Else reiterate until sorted

# Given array to sort
bubble_array = [2,4,5,10,7,3]
# Print original array before sorting
print(*bubble_array)
# Sorting algorithm (bubble sort)
bubbleSort(bubble_array)
# Print original array after sorting
print(*bubble_array)