# Separate alphabets and numbers from a string
# Input = "Sat123vik" -> Output = "Satvik, 123"


string = input("Enter a string : ")

alphabets = ""
numbers = ""

for char in string : 

    # If the character is an alphabet, add it to 'alphabets'
    if char.isalpha():
        alphabets += char

    # If the character is a digit, add it to 'numbers'
    elif char.isdigit():
        numbers += char

print(f"Result : {alphabets}, {numbers}")