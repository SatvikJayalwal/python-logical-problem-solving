# Sum of even integers in an array

arr = list(map(int, input("Enter numbers separated by space: ").split()))

sum_even = 0

for num in arr:
    if num % 2 == 0:    # check if number is even
        sum_even += num  # add to sum

print(f"Sum of even numbers in the array: {sum_even}")