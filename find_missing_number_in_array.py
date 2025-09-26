# Find missing single number in an array

arr = [1,2,4,5,6]
max = len(arr) + 1  # Because one number is missing

# Calculate total sum from 1 to max
total = max * (max + 1) // 2

# Calculate sum of array
sum_arr = sum(arr)

# Missing number
missing = total - sum_arr
print(f"The missing number is : {missing}")