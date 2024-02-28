# Task. Check if the entered word is a palindrome.
someWord= input("Enter the word:\n")
print(someWord[::1], someWord[::-1])
if someWord[::1] == someWord[::-1]:
    print("The word is a palindrome")
else:
    print("The word is not a palindrome")
