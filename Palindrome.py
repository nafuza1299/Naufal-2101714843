palindrome = "racecar"
palindrome_rv = reversed(palindrome)
if list(palindrome) == list(palindrome_rv):
    print("It is a palindrome")
else:
    print("It is not a palindrome")
