# Create a relationship between three lists where elements at the same index correspond

names = ["Monica", "Nimisha", "Ranish", "Aditi"]  # List of names
pins = [123001, 121212, 50001, 900000]          # Corresponding PIN numbers
codes = ["P1", "P2", "P3", "P4"]               # Corresponding codes

data = {}  # Initialize an empty dictionary to hold the combined data

# Loop through all three lists simultaneously using zip
for name, pin, code in zip(names, pins, codes):
    # Store each entry in the dictionary using PIN as the key
    # Each value is another dictionary containing the pin and code
    data[pin] = {"name": name, "code": code}

# Print the final combined dictionary
print(f"Data: {data}")