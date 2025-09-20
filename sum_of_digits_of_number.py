# Sum of digits of number

num = int(input("Enter a number : "))

temporary_num = num
digits_sum = 0

while temporary_num > 0 : 
    
    remainder = temporary_num % 10          # extract last digit
    digits_sum += remainder                 # add to sum
    temporary_num = temporary_num //10      # remove last digit 

print(f"Sum of digits of {num} is {digits_sum}")