# write a python program to take a 2 digit number as input and print sum of its digits.
number = int(input("Enter a 2 digit number: "))
if 10 <= number <= 99:
    digit1 = number // 10
    digit2 = number % 10
    sum_of_digits = digit1 + digit2
    print("Sum of digits:", sum_of_digits)
else:
    print("Please enter a valid 2 digit number.")   