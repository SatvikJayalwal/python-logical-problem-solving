# Reverse an array without using extra space

arr = [1, 2, 3, 4, 5]
print(f"Original array : {arr}")

# Set two pointers (start, end)
start = 0
end = len(arr) - 1

# Keep swapping elements until start crosses end
while start < end:

    # Swap the values
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp

    # Move start forward and end backward
    start += 1
    end -= 1

print("Reversed array:", arr)
