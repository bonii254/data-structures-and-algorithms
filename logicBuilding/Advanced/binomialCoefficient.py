import math


def binomialCoefficient(n, k):
    """
    C(n, k) = C(n-1, k-1) + C(n-1, k)
    recursive call
    """
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return binomialCoefficient(n - 1, k-1) + binomialCoefficient(n - 1, k)


print(binomialCoefficient(5, 6))


def binomialCoeff(n, k):
    """
    use build in comb
    """
    return math.comb(n, k)


print(binomialCoeff(5, 6))


def binomialCoefficienFactorial(n, k):
    """Using build in factorial"""
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

print(binomialCoefficienFactorial(5, 6))