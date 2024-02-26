#Task 1.
# Given real positive numbers a, b, c. It is necessary to find out whether there is a triangle with sides a, b, c.

# Solution
# 1) Assigning values to variables a,b,c:
a=int(input("Enter length for a:\n"))
b=int(input("Enter length for b:\n"))
c=int(input("Enter length for c:\n"))
# 2) Drawing up a condition
if a+b>c and a+c>b and b+c>a:
    print("Triagle with sides a, b, c exists")
else:
    print("Triangle with sides a, b, c is not exists")

# Task 2.
# An integer n is given (n ranges from 1 to 99), which determines the person's age in years.
# For this number you need to type the phrase “Мне n лет”.
# Keep in mind that for some values of n the word “лет” must be replaced with the word “год” or “года”.
# Solution
# 1) Assigning value to variable 'my_age'
my_age=int(input("Enter your age:\n"))
# 2) Drawing up a conditions
if my_age % 10 == 1:
    if my_age == 11:
        print('Мне '+ str(my_age) +' лет')
    else:
        print('Мне '+ str(my_age) +' год')
elif my_age % 10 < 5:
    if my_age >= 10 and my_age <= 20:
        print('Мне '+ str(my_age) +' лет')
    else:
        print('Мне ' + str(my_age) + ' года')
else:
    print('Мне ' + str(my_age) + ' лет')
