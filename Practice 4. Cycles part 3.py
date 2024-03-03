#  Task. A random ten-digit number comes to the input. Calculate the sum of its digits.
import random
number = random.randint(10**9,10**10)
print(number)
strnum = str(number)
summ=0
for i in range(0,len(strnum)):
    summ += int(strnum[i])
print(summ)
print('Task complete')