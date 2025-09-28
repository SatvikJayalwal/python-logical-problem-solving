# Find min and max from array 

# Short way ( Using built in function )
"""
arr = [1,3,5,10]

print(f"Min : {min(arr)}")
print(f"Max : {max(arr)}")
"""

# Long way
arr = [1,3,5,10]
min = arr[0]
max = arr[0]

for num in arr :

    if num < min :
        min = num

    if num > max : 
        max = num

print(f"Min : {min}")
print(f"Max : {max}")