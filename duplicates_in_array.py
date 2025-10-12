# Find duplicates with count in array

arr = [1, 2, 3, 2, 4, 1, 5, 2, 1]

count_dict = {}

for num in arr:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

# Print only duplicates
for key, value in count_dict.items():
    if value > 1:
        print(f"{key} appears {value} times")