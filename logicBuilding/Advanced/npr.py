def fact(num):
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

def permutation(n, r):
    if n < r:
        return "Invalid input: r cannot be greater than n"
    return fact(n) // fact(n - r)

n = int(input("Enter value of n: "))
r = int(input("Enter value of r: "))

print(f"The value of {n}P{r} is:", permutation(n, r))
