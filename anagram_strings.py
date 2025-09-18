# Anagram strings

# Take first string input and convert it to lowercase 
str1 = input("Enter first string : ").lower()  

# Take second string input and convert it to lowercase 
str2 = input("Enter second string : ").lower()  

# Sort the letters of both strings and compare

if sorted(str1) == sorted(str2):  
    # If equal, they are anagrams
    print(f"The strings {str1} and {str2} are Anagrams")  

else:  
    # If not equal, they are not anagrams
    print(f"The strings {str1} and {str2} are not Anagrams")  
    
