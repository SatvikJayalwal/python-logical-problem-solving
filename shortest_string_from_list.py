# Find shortest string  from list and show in uppcase 

words = ["apple", "banana", "watermelon", "mango", "grape", "kiwi"]

shortest = words[0]

for word in words :

    if len(word) < len(shortest) :
        shortest = word

print(f"Shortest word: {shortest.upper()}")