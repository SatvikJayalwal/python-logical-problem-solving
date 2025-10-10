# Find the first non-repeated character in a string

from collections import Counter

str = "swiss"

count = Counter(str)

first_non_repeated = None

for ch in str :

    if count[ch] == 1 :
        first_non_repeated = ch
        break

print(f"First non repeated character : {first_non_repeated}")