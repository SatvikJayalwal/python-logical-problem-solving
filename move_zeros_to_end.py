# Move all zeros to the end of a string of digits, while keeping the order of the non-zero digits 
# Eg. Input string  = "32400121200" , output string =  "324121200000" 

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

# Combine non-zero digits first, then all zeros at the end
print("Result : ",numbers+zeros)