# Sum only integers from a mixed array

arr = [10, "#", 60, "$", 50]
sum = 0

for num in arr : 
    if isinstance(num,int):  # Check if item is integer
        sum += num

print(f"Sum : {sum}")