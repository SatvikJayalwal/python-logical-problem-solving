# Line reverse 

sentence = "This is interview question"

# Split sentence into words
words = sentence.split()  

# Reverse the list of words
words.reverse()  

# Join words back into a string
reversed_sentence = " ".join(words)

print(f"Original sentence : {sentence}")
print(f"Reversed sentence : {reversed_sentence}")