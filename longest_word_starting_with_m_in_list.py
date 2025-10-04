# Longest Word Starting with m

words = ["apple", "ber", "mashroom","mango", "watermelon", "grape"]

count = 0 
longest = ""

for word in words :

    word_len = len(word)
    longest_word_len = len(longest)

    if word[0] == "m" :

        if word_len > longest_word_len :
            count = word_len
            longest = word
        
print(f"Longest word starting with 'm' : {longest}")
print(f"Count : {count} letters in it")