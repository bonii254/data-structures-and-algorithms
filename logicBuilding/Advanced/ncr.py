def fact(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def nCr(n, r):
    if r > n:
        return "Invalid input: r cannot be greater than n"
    return fact(n) // (fact(r) * fact(n - r))

n = int(input("Enter value of n: "))
r = int(input("Enter value of r: "))

print(f"The value of {n}C{r} is:", nCr(n, r))