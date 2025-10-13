# String reverse

str = "Satvik Jayalwal"
rev = ""

# Loop from last index to 0
for i in range(len(str)-1, -1, -1):  # Start at last index, end at 0, step -1
    rev += str[i]  # Add current character to rev

print(f"Original string : {str}")
print(f"Reversed string : {rev}")