"""euclidean algorithm"""


def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a < b:
        return gcd(a, b - a)
    return gcd(a - b, b)       

a = 20
b = 28
print(gcd(a, b))