# Search element in an array (Linear Search)

arr = [10, 25, 30, 45, 50]
target = 30   # Element to be searched

# Flag to check if element is found
found = False

# Loop through the array
for i in range(len(arr)):
    if arr[i] == target:
        print(f"Element {target} found at index {i}")
        found = True
        break   # Stop after finding the element

if not found:
    print(f"Element {target} not found in array")