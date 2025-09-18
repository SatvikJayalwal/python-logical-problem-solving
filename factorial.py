# Factorial

# Shorter way : 
"""
import math

num = int(input("Enter a number : "))

print(f"Factorial of {num} is : ", end=" ")

print(math.factorial(num))
"""

# Longer way :
num = int(input("Enter a number : "))

# Save the original number (because we will decrease num later)
original_num = num 

# Factorial of 0 is always 1
if num == 0:
    print("0! == 1")

# Factorial of numbers greater than 1
elif num > 1:
    fact = 1

    while num > 0:
        fact = fact * num

        # For the last number, don’t print '*'
        if num == 1:
            print(f"{num}", end = " ")

        # For other numbers, print with '*'
        else:
            print(f"{num} * ", end = "")

        num = num -1     
         
    print(f"= {fact}")


