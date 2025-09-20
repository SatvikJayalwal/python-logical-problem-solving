# Reseverse string in same order of words 

# Shorter way
"""
sentence = input("Enter a sentence : ")
print(" ".join(word[::-1] for word in sentence.split()))
"""

# Longer way
sentence = input("Enter a sentence : ")

words = sentence.split()

reversed_words = []

for word in words:
    reverse_word = word[::-1]
    reversed_words.append(reverse_word)

result = " ".join(reversed_words)

print(f"Reversed words string : {result}")