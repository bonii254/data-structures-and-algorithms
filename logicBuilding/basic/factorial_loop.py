def factorial(number):
    ans = 1
    i = 2
    while i <= number:
        ans *= i
        i += 1
    return ans

print(factorial(0))