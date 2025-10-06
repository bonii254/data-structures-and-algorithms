def ifArmstrong(number):
    length = len(str(number))
    sum = 0
    for i in range(length):
        num = int(str(number)[i])
        sum += pow(num, length)
    return sum == number


def is_armstrong(number: int) -> bool:
    """Check if a number is armstrong"""
    digits = str(number)
    power = len(digits)
    total = sum(int(d)**power for d in digits)
    total == number

print(ifArmstrong(1634))