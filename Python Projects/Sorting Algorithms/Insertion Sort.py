# Original array
array = [5, 1, 4, 7, 9]

# Traverse through 1 to len(array)
for i in range(1, len(array)):
    # Store the current element to be compared
    key = array[i]

    # Move elements of array[0..i-1] that are greater than key
    # to one position ahead of their current position

    # j is used to compare the value before the key to sort
    j = i - 1
    # As long as j is not a negative number then iterate through the array
    # and carry on if the key is one item behind variable j
    while j >= 0 and key < array[j]:
        # If such is true, then shift the current value by one, sorting it
        array[j + 1] = array[j]
        # Decrement j by 1 to move to the previous position (starts from end of list)
        # and then redo shifting process with rest of the numbers
        j -= 1

    # Insert the key at its correct position in the sorted sequence
    # Add 1 to j because it was just decremented, but the value has been sorted
    # So now we assign the key to that correct position
    array[j + 1] = key

    # Print the array at each step
    print(f"Step {i}: {array}")

# Print the final sorted array
print("\nFinal Sorted Array:", *array)
