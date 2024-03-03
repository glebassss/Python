# Task 1. Display as many elements of the Fibonacci series as specified by the user.
# For example, if the input is the number 6, then the output should contain the first six numbers of the Fibonacci series: 1 2 3 5 8 13.

amount = int(input("Enter amount of Fibonacci numbers: "))
i = 1
j = 1
while amount!=0:
    i, j = j, i+j
    print(i)
    amount -= 1
print('Task 1 completed')

# 2. Calculate the factorial of the entered number.
import math
print(math.factorial(int(input('Enter a number: '))))
print("Task 2 completed")