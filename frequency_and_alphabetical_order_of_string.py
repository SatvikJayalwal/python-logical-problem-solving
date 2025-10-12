string = "alphabetical"

# Create an empty dictionary
freq = {}

# Count frequency of each character
for char in string:
    freq[char] = freq.get(char, 0) + 1

# Sort by character and print
for char in sorted(freq):
    print(f"{char}: {freq[char]}")