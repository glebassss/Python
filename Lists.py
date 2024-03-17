# Task 1. Given a list containing positive and negative integers, calculate the sum of the even positive elements.
my_list = [1,-2,-3,4,-5,6,7,8,-9]
summ = 0
for i in my_list:
    if i % 2 == 0 and i > 0:
        summ = summ + i
print('The sum of the numbers is: ', summ)
print('Task 1 is complete!')

# Task 2. Find in the list those elements whose value is less than the arithmetic mean taken from all elements of the list.
my_list = list(range(1000))
arithmetic_mean = sum(my_list)/len(my_list)
print('arithmetic mean: ', arithmetic_mean)
for item in my_list:
    if item<arithmetic_mean:
        print(item)
print('Task 2 is complete!')


