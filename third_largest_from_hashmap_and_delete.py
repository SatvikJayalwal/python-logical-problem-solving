# Find third largest from a hashmap and delete that element

# Create a Dictionary 
data = {
    101 : "Riya",
    102 : "Janvi",
    103 : "Tannu",
    106 : "Monika",
    105 : "Muskan"
}

print(f"Original data : {data}")

# Get all keys
keys = list(data.keys())          # Convert the dictionary keys into a list
print("All keys:", keys)

# Sort the keys in descending order
keys.sort(reverse=True)           # Sort from largest to smallest
print("Keys sorted in descending order:", keys)

# Find the 3rd largest key (index 2, since index starts from 0)
third_largest_key = keys[2]
print("3rd largest key:", third_largest_key)

# Remove the key-value pair for the 3rd largest key
data.pop(third_largest_key)

# Show updated dictionary
print("After deleting 3rd largest key:", data)