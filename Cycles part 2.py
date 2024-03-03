# Task. Find the sum of elements between the minimum and maximum elements.
# The minimum and maximum elements themselves are not included in the amount.
minimum = int(input("Enter the minimum: "))
maximum = int(input('Enter the maximum: '))
summ = 0
for number in range(minimum+1, maximum):
    summ += number
print(summ)

