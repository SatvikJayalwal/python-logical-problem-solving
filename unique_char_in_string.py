# Print unique character in a string

# Take input string and convert to lowercase
string = input("Enter a string : ").lower()

# Loop through each character in string
for char in string :
    if string.count(char)==1:
        print(char,end="")



