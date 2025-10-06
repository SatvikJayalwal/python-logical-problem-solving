# Find the first non-repeating character in a string

string = "find first non repeating char in the string"

# Loop through each character in the string
for ch in string :

    # Ignore spaces
    if ch == " " :
        continue

    # Check if this character appears only once
    if string.count(ch) == 1 :
        print(f"The first non repeating char in the string : {ch}")
        break