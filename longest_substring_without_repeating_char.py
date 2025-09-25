# Longest Substring Without Repeating Characters
# Eg. Input = "abcabcbb" Output = "abc" and length = 3

string = input("Enter a string : ")

longest = ""   # Stores longest unique substring
current = ""   # Stores current unique substring

for char in string:

    if char in current:  
        # Cut string after previous same char
        current = current[current.index(char)+1:]

    current += char   # add current char

    if len(current) > len(longest):  
        # Update longest if current is bigger
        longest = current 

print(f"Longest substring without repeating chars: {longest}")
print(f"Length: {len(longest)}")
