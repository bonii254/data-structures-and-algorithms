def divisibleBy4(num):
    if num == 0:
        return False
    last_two_digits = int(str(num)[-2:]) if abs(num) >= 100 else abs(num)
    return last_two_digits % 4 == 0


print(divisibleBy4(8))     # True
print(divisibleBy4(12))    # True
print(divisibleBy4(1232))  # True
print(divisibleBy4(1233))  # False
print(divisibleBy4(-16))   # True
print(divisibleBy4(0))     # False