# Reverse String Keeping Special Characters the same

string = "a@b#c$D%*()^"

# Take only the letters from the string
letters = ""
for ch in string:
    if ch.isalpha():           # Check if the character is a letter 
        letters += ch

# Reverse all the letters
letters = letters[::-1]

# Loop original string again and rebuild it by replacing only letters with reversed ones
result = ""
index = 0   # To track position in the reversed letters

for ch in string:
    if ch.isalpha():    # If it’s a letter → take from reversed letters
        result += letters[index]
        index += 1

    else:   # If it’s a special char → keep as it is
        result += ch

# Show the result
print(f"Original: {string}")
print(f"Result:  {result}")