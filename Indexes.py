#Using slices, this displays:
number=('1234566789')
print(number[::])   #the whole list
print(number[1::2])  #elements odd in order
print(number[::2]) #elements even in order
print(number[::-1]) #all elements in reverse order
print(number[6::])  #all elements starting from the sixth
print(number[:6])   #all elements, not reaching the sixth
print(number[-2:3:-1])  # all elements from the penultimate to the third in reverse order