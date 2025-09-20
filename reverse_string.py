# Reverse String

# Shorter way
"""
string = input("Enter a string : ")
reversed_str = string[::-1]
print(f"Reversed String : {reversed_str}")
"""

# Longer way
string = input("Enter a string : ")
reversed_str = ""

# Loop through each character in the string
for char in string:
    reversed_str = char + reversed_str

print(f"Reversed string : {reversed_str}")