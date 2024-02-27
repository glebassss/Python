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
    print('Task 1 complete')

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
print('Task 2 complete')