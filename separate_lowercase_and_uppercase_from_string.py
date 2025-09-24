# Separate lowercase and uppercase letters from a string and print them in sorted order
# Input = "aBACbcEDed" -> Output = "abcde, ABCDE"

string = input("Enter a string : ")

lowercase = ""
uppercase = ""

for char in string :
    
    if char.islower() :
        lowercase += char

    elif char.isupper() :
        uppercase += char

# Convert lowercase/uppecase into a set (to remove duplicates),then sort it, then join back into a string
sorted_lowercase = "".join(sorted(set(lowercase)))
sorted_uppercase = "".join(sorted(set(uppercase)))

print(f"Result : {sorted_lowercase}, {sorted_uppercase}")


