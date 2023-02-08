def palindrom():
    pal = str(input("Enter a word to check if it is a palindrome: "))
    if pal == pal[::-1]:
        return True
    else:
        return False

print(palindrom())
