# Find the longest word in a list

words = ["apple", "banana", "cherry", "mango", "watermelon", "mashroom", "grape"]

count = 0 
longest_word = ""

for word in words :

    if len(word) > len(longest_word) : 
        count = len(word)
        longest_word = word

print(f"Longest word : {longest_word}")
print(f"Length : {count}")
