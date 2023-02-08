def palindrom():
    """
    Returned true or false based on checking if the user supplied word is a palindrome.
    """
    pal = str(input("Enter a word to check if it is a palindrome: "))
    if pal == pal[::-1]:
        return True
    else:
        return False

print(palindrom())
