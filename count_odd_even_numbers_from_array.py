# Count odd and even numbers from array 

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd = []
even = []

for num in arr : 

    if num % 2 == 0 : 
        even.append(num)

    else:
        odd.append(num)

print(f"Odd : {odd}")
print(f"Even : {even}")