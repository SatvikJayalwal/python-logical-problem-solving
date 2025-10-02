# Reverse all digits but keep the decimal in the same position

num = input("Enter a decimal number: ")  # E.g (1234.56)

# Remove the decimal
cleaned = num.replace(".", "")

# Reverse all digits
rev = cleaned[::-1]

# Find decimal position from the end
decimal_pos = len(num) - num.index(".") - 1

# Insert decimal back at the same position
result = rev[:-decimal_pos] + "." + rev[-decimal_pos:]

print(f"Result: {result}")