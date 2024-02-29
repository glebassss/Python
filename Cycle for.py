#Task 1. Find the sum and product of the digits of the entered three-digit natural number.
# For example, if the number 325 is entered, then the sum of its digits is 10 (3+2+5), and the product is 301 (325).
number = input("Enter a number: ")
if len(number)==3:
        Sum = 0
        Prod = 1
        try:
            for i in number:
                Sum += int(i)
                Prod *= int(i)
            print('The sum is', Sum, '\nThe prod is', Prod)
            print('Task 1 complete!\n')
        except ValueError:
            print("Please enter a three-digit number")
else:
    print('Please enter a three-digit number')

# 2. Display a series of natural numbers from minimum to maximum in increments.
# For example, if the minimum is 10, the maximum is 35, the step is 5, then the output should be like this: 10 15 20 25 30 35.
# The minimum, maximum and step are specified by the user (read from the keyboard).
try:
    Minimum = int(input("Enter the minimum: "))
    Maximum = int(input("Enter the maximum: "))
    for j in range(Minimum,Maximum+1, 5):
        print(j)
    print('Task 2 complete!')
except ValueError:
    print("Please, enter a number")