# Find duplicates with count in array

arr = [5, 9, 3, 6, 4, 9, 5]

duplicates = {}   # dictionary to store number -> count

for num in arr:
    if num in duplicates:
        duplicates[num] += 1
    else:
        duplicates[num] = 1

# Now print only those that appeared more than once
for num, count in duplicates.items():
    if count > 1:
        print(f"{num} appears {count} times")