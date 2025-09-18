# Armstrong Number

# Take input from user
num = int(input("Enter a number : "))

# Count the number of digits
digits = len(str(num))
print(f"Digits in {num} = {digits}")

# Convert number to string to access each digit by index
num_str = str(num)

# Initialize total sum
total = 0

# Loop through each digit by index
for i in range(len(num_str)):
    d = int(num_str[i])  # Convert string digit to integer

    # Print each digit raised to power of total digits
    # Add '+' only if it is not the last digit
    if i == len(num_str) - 1:
        print(f"{d}^{digits}", end="")
    else:
        print(f"{d}^{digits} + ", end="")

    # Add digit^digits to total sum
    total += d ** digits

# Print the sum after the loop
print(f" = {total}")

# Check if the number is Armstrong
if total == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is NOT an Armstrong number")
