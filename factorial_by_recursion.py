# Factorial by recursion

def factorial_of_num(n):

    # If n = 0 or 1, factorial is always 1
    if n == 0 or n == 1:
        return 1
    
    # If n > 1, multiply n by factorial of (n-1)
    if n > 1:
        return n * factorial_of_num(n - 1)

num = int(input("Enter a number: "))

print(f"Factorial of {num} is {factorial_of_num(num)}")