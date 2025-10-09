import math


def getAllDivisors(num):
    factors = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            if num // i == i:
                factors.append(i)
            else:
                factors.append(i)
                factors.append(num // i)
    return sorted(factors)

print(getAllDivisors(100))