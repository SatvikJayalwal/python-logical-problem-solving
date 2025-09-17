# Fibonacci Series 0, 1, 1, 2, 3, 5, 8, 13, 21 …

num = int(input("Enter number of terms : "))

a,b = 0,1

for i in range(num):
    print(a," ")
    a,b = b, a+b   # a becomes b, b becomes (a+b) using OLD values
    

