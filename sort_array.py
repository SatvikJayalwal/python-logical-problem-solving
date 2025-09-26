# Sort an array

# Shorter way (Using Python's built-in sorted function)
"""
arr = [5, 2, 9, 1, 7]

# sorted() returns a new sorted list from the original list
sorted_arr = sorted(arr)

# Print original and sorted arrays
print(f"Original array : {arr}")
print(f"Sorted array : {sorted_arr}")
"""

# Longer way (Using Bubble Sort : manual sorting)
arr = [1, 2, 5, 7, 9]

# Outer loop (We repeat the process for every element)
for i in range(len(arr)):

    # Inner loop (Compare each pair of adjacent elements)
    for j in range(len(arr)-1):
        
        # If left element is greater than right element, swap them
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(f"Sorted array : {arr}")