# Find the character count in a string "Steve Jobs" by ignoring space in between

str = "Steve Jobs"
count = 0

for ch in str:
    if ch.isalpha():
        count += 1

print(f"String : {str}")
print(f"Count of characters by ignoring space : {count}")