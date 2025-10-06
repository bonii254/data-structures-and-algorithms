from lcm_gcd import lcm, gcd


def addFraction(a, b):
    den = lcm(a[1], b[1])
    num = a[0] + b[0]
    
    common_factor = gcd(num, den)
    num //= common_factor
    den //= common_factor
    
    return [num, den]

a = [1, 2]
b = [3, 2]

ans = addFraction(a, b)
print(f'{ans[0]}, {ans[1]}')