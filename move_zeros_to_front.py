# # Move all zeros to the front of a string of digits, while keeping the order of the non-zero digits 
# Eg. Input string  = "32400121200" , output string =  "000003241212" 

string = input("Enter a string of digits : ")

numbers = ""  # It will store digits that are not zero
zeros = ""    # It will store only zeros

for char in string :

    # If the character is not zero, add it to the 'numbers' string
    if char != "0" :
        numbers += char

    # If the character is zero, add it to the 'zeros' string
    elif char == "0" : 
        zeros += char

# Combine zeros first, then all non-zero digits at the end
print("Result : ",zeros+numbers)
        