# Find all permutations of a given string (Eg. abc = abc, acb, bac, bca, cab, cba)

from itertools import permutations

string = input("Enter a string : ")
perms = set(permutations(string))       # Removes duplicates

counter = 0

for perm in perms :
    counter += 1
    print("".join(perm))    # Convert tuple to string and print

print(f"The total number of permutations of the given string : {counter}")
