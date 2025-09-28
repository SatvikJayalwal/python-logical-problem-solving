# Filter numbers between 1 and 9 from an array
arr = [11223, 4, 55, 66, 333]

result = []

for num in arr :

    # Convert each number to string and check if its length is 1
    if len(str(num)) == 1 :
        result.append(num)

print(f"Result : {result}")