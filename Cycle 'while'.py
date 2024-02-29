#Task 1. There is a five-digit natural number.
# Find its largest number.
# For example: the number 76458 is entered, the largest digit in it is 8.
print('For exit press C')
while True:
    Enter = input("Enter a five-digit number: ")
    if Enter.lower() == 'c':
        print('Exit the program')
        break
    if len(Enter) == 5:
        print('Max digit is: ', max(Enter))
    else:
        print('Please enter a five-digit number')
print('Task 1 complete\n')

# 2. Form the entered number into the reverse order of its digits and display it on the screen.
# For example: the number 3486 is entered, then you need to output the number 6843.
print('For exit press C')
while True:
    Enter = input("Enter a number: ")
    if Enter.lower() == 'c':
        print('Exit the program')
        break
    print(Enter[::-1])