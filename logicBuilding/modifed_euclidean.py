"""euclidean algorithm"""


def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a < b:
        if b % a == 0:
            return a
        return gcd(a, b - a)
    if a % b == 0:
            return b
    return gcd(a - b, b)       

a = 20
b = 28
print(gcd(a, b))