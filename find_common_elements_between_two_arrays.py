# Find common elements between two arrays

# Short way ( Using sets )
"""
arr1 = [1,2,3,4,5,6]
arr2 = [4,5,6,7,8,9]

# Turn both into sets (unique only), find intersection
common = list(set(arr1) & set(arr2))

print(f"Common elements: {common}")
"""

# Long way ( Using Loops )
# Take input arrays
arr1 = [1,2,3,4,5,6]
arr2 = [4,5,6,7,8,9]

common = []

for num in arr1 : 

    if num in arr2 and num not in common :
        common.append(num)

print(f"Common elements: {common}")