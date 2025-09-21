# Count the number of words in a string

string = input("Enter a sentence : ")

words = string.split()      # break the sentence into words
count = len(words)          # count how many words are there

print(f"The number of words in given string : {count}")