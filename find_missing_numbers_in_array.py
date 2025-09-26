# Find missing numbers from an array

arr = [1, 2, 4, 6]   
max = 6                

# Create a set of all numbers from 1 to max
full_set = set(range(1, max+1))

arr_set = set(arr)

# Numbers in full_set but not in arr_set
missing = list(full_set - arr_set)

print(f"Missing numbers: {missing}")