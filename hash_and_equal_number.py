# Python program to implement hashcode and equals

a = "hello"
b = "hello"
c = "world"

# Check equality
print(a == b)  # True 
print(a == c)  # False 

# Hash values (special numbers Python gives)
print(hash(a))  # some number
print(hash(b))  # same as hash(a)
print(hash(c))  # different number
