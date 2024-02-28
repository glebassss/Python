#  Task. Find out if the entered number is divisible by 5
try:
    entered_number = int(input('Enter a number: '))
except ValueError:
    print('Invalid value. Please, enter a number.')
else:
    if entered_number % 5 == 0:
        print('The entered number is divisible by 5')
    else:
        print("The entered number isn't divisible by 5")