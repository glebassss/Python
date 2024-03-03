# Task. The user enters the number n. Find all prime numbers up to this number
n = int(input('Enter a number: '))
for i in range(1,n+1):
    divivers = 0
    for j in range(1, i+1):
        if i%j == 0:
            divivers +=1
    if divivers == 2:
        print(i)
