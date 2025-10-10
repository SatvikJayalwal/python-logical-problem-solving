# Convert Small letters to capital letters and capital letters to small letters in a string 

# Shorter way
"""
str = "ABC xyz"
result = str.swapcase()

print(f"String : {str}")
print(f"Result : {result}")
"""

# Longer way
str = "ABC xyz"

result = ""

for i in str :

    if i.isupper() :
        i = i.lower()
        result += i

    else :
        i = i.upper()
        result += i

print(f"String : {str}")
print(f"Result : {result}")