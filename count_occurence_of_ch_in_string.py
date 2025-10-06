# Count occurrences of a character in a string 

string = "abcaaabbccccccab"

# Create an empty dictionary to store character counts
count_dict = {}

# Go through each character one by one
for ch in string:

    # If character already exists in dictionary, increase its count
    if ch in count_dict:
        count_dict[ch] += 1

    # Else add it to dictionary with count 1
    else:
        count_dict[ch] = 1

print(count_dict)