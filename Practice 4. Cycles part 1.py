#  Task. The user enters a number 'n'.
#  Find and print all perfect numbers up to this number
n=int(input("Enter the number: "))
for i in range(1,n+1):
    divider = 0
    for j in range(1,i):
        if i%j == 0:
            divider+=j
    if divider == i:
        print(i)
print('Task complete')