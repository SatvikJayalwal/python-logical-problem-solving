# Print even indexed characters in a string

string = input("Enter a string : ")

print("Characters at even indexes: ")

for i in range(0, len(string)):
    if i % 2 == 0:   # Check if index is even
        print(string[i], end=" ")