# Task. The user enters the height of the triangle. Construct a right triangle
height = int(input("Enter a height of triangle: "))
for i in range(height+1):
    print("*"*i, end="\n")
print('Task complete')