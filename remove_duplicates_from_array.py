# Remove duplicates from an array

# Short way ( Using sets )
"""
arr = [1,2,2,3,4,4,5]
unique_arr = list(set(arr))

print(f"Unique array : {unique_arr}")
"""

# Longer way
arr = [1,2,2,3,4,4,5]

unique_arr = []

for num in arr :
    
    if num not in unique_arr :
        unique_arr.append(num)

print(f"Unique array : {unique_arr}")