# Remove special characters from string

str = "A$##B%^###&$%^C$#$D!&*@@"

result = ""
for ch in str :

    if ch.isalpha() :
        result += ch
 
print(f"Original string : {str}")
print(f"Clear string : {result}")