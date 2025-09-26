# Find duplicate numbers in array

arr = [1, 2, 2, 3, 4, 4, 5]

duplicates = []
seen = []  # Track numbers we have already seen

for num in arr:

    if num in seen and num not in duplicates:
        duplicates.append(num)  # Add to duplicates if seen before
    else:
        seen.append(num)  # First time seen, add to seen list

print(f"Duplicate numbers (long way): {duplicates}")