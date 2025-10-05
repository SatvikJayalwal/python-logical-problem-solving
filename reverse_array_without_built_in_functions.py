# Reverse a ARRAY without using built-in functions

# Original array
arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Create an empty array to store reversed elements
reversed_arr = []

for i in range(len(arr)-1, -1, -1):
    reversed_arr.append(arr[i])

print("Original array:", arr)
print("Reversed array:", reversed_arr)