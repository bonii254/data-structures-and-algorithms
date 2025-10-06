def squareRoot(number):
    """Using a loop - O(sqrt(n)) Time and O(1) Space"""
    n = 1
    while n * n <= number:
        n += 1
    return n - 1

print(squareRoot(100))