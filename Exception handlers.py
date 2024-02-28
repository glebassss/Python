from datetime import datetime, date

# Task 1. 1. Create and handle exceptions for TypeError and ValueError.
numberOne = 10
numberTwo = 'Twenty'
try:
    print(numberOne+numberTwo)
except TypeError:
    print('Different data types')
    try:
        print(numberOne+int(numberTwo))
    except ValueError:
        print('Wrong value in "numberTwo", change it to integer')
finally:
    print('Task 1 complete\n')

# Task 2. The year, month number and day of birth of a person are known,
# as well as the day, year and month number of today. Determine the person's age (number of completed years).
currentDay = datetime.date(datetime.today())
print(currentDay)
year = input('Enter a year: ')
month = input('Enter a month: ')
day = input('Enter a day: ')
birthDay = date(int(year), int(month), int(day))
print(birthDay)
personDay = currentDay - birthDay
print(personDay)
personYear = personDay.days//365
print('The person is ' + str(personYear) + ' y.o.')
print('Task 2 complete\n')

# Task 3. The year, month number and birthday of each of the two people are known.
# Determine which of them is older.
FirstYear = input('First person. Enter a year : ')
FirstMonth = input('First person. Enter a month: ')
FirstDay = input('First person. Enter a day: ')
FirstBirthday = date(int(FirstYear), int(FirstMonth), int(FirstDay))
print(FirstBirthday)
SecondYear = input('Second person. Enter a year : ')
SecondMonth = input('Second person. Enter a month: ')
SecondDay = input('Second person. Enter a day: ')
SecondBirthday = date(int(SecondYear), int(SecondMonth), int(SecondDay))
print(SecondBirthday)
Differense= FirstBirthday-SecondBirthday
if Differense.days > 0:
    print('The Second person is older than the First person')
else:
    print('The First Person is older than the Second person')