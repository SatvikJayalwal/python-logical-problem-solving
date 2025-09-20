# Find which character is repeated the most and how many times it appears in a given string

from collections import Counter

string = input("Enter a string : ").replace(" ", "")  # remove spaces

# Count frequency of each character
counter = Counter(string)

# Find the most common character
most_common_char, freq = counter.most_common(1)[0]

print(f"The most repeated character is '{most_common_char}' with {freq} occurrences")