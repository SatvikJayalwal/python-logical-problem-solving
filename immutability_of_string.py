# Immutability of String

s1 = "hello"
s2 = "hello"  #point to the same memory address

print("id of s1:", id(s1))
print("id of s2:", id(s2))

print("s1 is s2 : ", s1 is s2)   

s1 = s1 + " world"
print(s1)
print(s2)

print("id of s1:", id(s1))
print("id of s2:", id(s2))