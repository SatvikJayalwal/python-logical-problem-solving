# Print each letter twice in a given string

string = input("Enter a string : ")

result = ""

for char in string:
    result += char * 2   # repeat each character twice

print(f"String with letters doubled: {result}")