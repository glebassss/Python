# Task 1. In a one-dimensional array of integers, determine the two smallest elements.
# They can be either equal to each other (both are minimal) or different.
# list=[]
# print('To stop enter the numbers press "y"')
# while True:
#     number=input("Enter a number: ")
#     if number=='y':
#         break
#     else:
#         list.append(int(number))
# list.sort()
# print('Two smallest numbers in list is: ', list[0], 'and ', list[1])
# print('Task 1 is completed successfully!')

# Task 2. Compress the array by removing from it all elements whose value is in the interval [a, b].
# Fill the vacated elements at the end of the array with zeros.
list_second=[1, 15, 46, 7, 13, 5, 2, 13, 22, 55, 76, 46, 13]
# print('To stop enter the numbers press "y"')
# while True:
#     number=input("Enter a number: ")
#     if number=='y':
#         break
#     elif number=='':
#         continue
#     else:
#         list_second.append(int(number))
print('List is', list_second)
lenght_list_before = len(list_second)
print(lenght_list_before)
start = int(input("Enter the start: "))
stop = int(input("Enter the stop: "))
list_third=[]
for i in list_second:
    if i >= start and i <= stop:
        list_third.append(i)
print(list_third)
lenght_list_after = len(list_third)
while lenght_list_before!=lenght_list_after:
    list_third.append(0)
    lenght_list_after+=1
print(list_third)
print('Task 2 completed')