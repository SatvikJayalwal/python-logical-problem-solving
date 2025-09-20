# Digits of Number

# Shorter way
"""
num = int(input("Enter a number : "))
digits_of_num = (len(str(num)))

print(f"Number of digits in {num} is {digits_of_num}")
"""

# Longer way
num = int(input("Enter a number : "))
digits_of_num = 0
temporary_num = num

while temporary_num > 0 :
    digits_of_num += 1
    temporary_num = temporary_num // 10

print(f"Number of digits in {num} is {digits_of_num}")
