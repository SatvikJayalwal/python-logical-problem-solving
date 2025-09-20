# Reverse Number

# Shorter way
"""
num = int(input("Enter a number : "))
rev = str(num)[::-1]
print(rev)
"""

# Longer way

num = int(input("Enter the number : "))
reversed_num = 0   # this will hold the final reversed number

# Loop until all digits are processed
while num > 0:  

    remainder = num % 10                          # Get the last digit
    reversed_num = reversed_num * 10 + remainder  # shift left and add last digit
    num = num // 10                               # remove the last digit from num

print(f"Reversed Number : {reversed_num}")
