# Count vowels and consonants in a string

# Take input from the user and convert it to lowercase
string = input("Enter a string : ").lower()

# Define all vowels
vowels = 'aeiou'

# Initialize counters for vowels and consonants
vowels_count = 0
consonant_count = 0

# Loop through each character in the string
for char in string:

    if char.isalpha():  # Check if the character is a letter

        if char in vowels:  # Check if the letter is a vowel

            vowels_count += 1  # Increment vowel count

        else:  # If it is a letter but not a vowel, it is a consonant
            
            consonant_count += 1  # Increment consonant count

# Print the total number of vowels and consonants
print(f"Total vowels in string : {vowels_count}")
print(f"Total consonants in string : {consonant_count}")
