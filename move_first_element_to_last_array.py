# Move the first element to the last

arr = [3, 4, 5, 6, 7, 8]
print("Original array:", arr)

# remove the first element
first = arr.pop(0)

# Add that element to the end
arr.append(first)

print("Result:", arr)
