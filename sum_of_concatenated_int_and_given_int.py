# Calculate the sum of the concatenated integer and the given integer  # Output = 126+9 = 135

arr = [1,2,6]
num = 9
conct = ""

for i in arr :

    conct += str(i)
    
result = int(conct) + num
print(f"Result : {result}")  