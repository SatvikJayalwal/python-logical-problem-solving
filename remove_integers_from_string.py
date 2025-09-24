# Remove integers from string

string = input("Enter a string : ")

result = ""

for char in string :
    
    # If the character is an alphabet (ignores digits and other chars)
    if char.isalpha() :
        result += char

print(f"Result : {result}")