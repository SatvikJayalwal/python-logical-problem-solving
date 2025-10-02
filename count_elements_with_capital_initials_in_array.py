# Count all elements in array whose first letter is capital

cities = ["Goa","rajasthan","Delhi","haryana","Banglore"]
print(f"Original cities : {cities}")

# Counter for capital first letters 
count = 0 

# Loop through each city
for city in cities :

    # Check if the first character is uppercase
    if city[0].isupper() :
        count +=1
        print(f"City : {city} and Index : {len(city)}") 

print(f"Total cities with capital first letter: {count}")