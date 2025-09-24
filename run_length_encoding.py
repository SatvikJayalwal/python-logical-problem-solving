# RLE (Run length encoding) (Eg. Input = aabbcccddddd -> Output= a2b2c3d5)

string = input("Enter a string: ")

encoded_str = ""

# Start with count = 1 (since first character is already seen once)
count = 1

# Loop from the 2nd character (index 1) to the end of the string
for i in range(1,len(string)) :

    # If current char is same as the previous one then increase count
    if string[i] == string[i - 1] :
        count += 1

    # Else (previous sequence ended), store char + count in result
    else : 
        encoded_str += string[i - 1] + str(count)
        count = 1

# After loop ends, Add the last character and its count
encoded_str += string[-1] + str(count) 

print(f"Encoded string : {encoded_str}")