# Task. The user enters a 3-digit number. Calculate the sum of the digits of this number.
# Add an exception
try:
    number1 = int(input("Enter a number: "))
except ValueError:
    print("Invalid value. Please enter a number.")
else:
    x=0
    for i in str(number1):
        x+=int(i)
    print(x)