def divisibleBy11(num):
    """
    check the difference of sum of digits at odd places 
    and sum of digits at even places is divisible by 11
    """
    num = abs(num)
    digits = list(map(int, str(num)))
    odds_sum = sum(digits[1::2])
    even_sum = sum(digits[::2])
    return abs(odds_sum - even_sum) % 11 == 0

print(divisibleBy11(121))   # True (1-2+1=0)
print(divisibleBy11(-1234321)) # True
print(divisibleBy11(12345)) # False
print(divisibleBy11(0))     # True (0 is divisible by 11)