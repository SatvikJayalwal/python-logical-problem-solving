# Find the maximum number from the array

# Short way
"""
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"Original array : {arr}")

max_num = max(arr)

print(f"Maximum number : {max_num}")
"""

# Long way
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"Original array : {arr}")

max_num = arr[0]

for num in arr :

    if num > max_num :
        max_num = num 

print(f"Maximum number : {max_num}")