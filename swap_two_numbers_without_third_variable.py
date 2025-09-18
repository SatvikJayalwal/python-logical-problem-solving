# Swap two numbers without using third variable

# Short way (Swap values at the same time)
"""
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

num1,num2 = num2, num1
print(f"Swaped first number : {num1}")
print(f"Swaped second number : {num2}")
"""

# Arithmatic way(Using +,-)
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

num1 = num1+num2
num2 = num1-num2
num1 = num1-num2
print(f"Swaped first number : {num1}")
print(f"Swaped second number : {num2}")
