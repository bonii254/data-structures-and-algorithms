def is_palidrome(number):
    """Check if a number is Palindrome"""
    return int(str(number)[::-1]) == number


def isPalidrome(number):
    numstring = str(number)
    length = len(numstring)
    for i in range(length // 2):
        if numstring[i] != numstring[length - i - 1]:
            return False
    return True

print(is_palidrome(121))
print(isPalidrome(121))