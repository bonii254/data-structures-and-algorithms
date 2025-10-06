def lcm(a, b):
    g = max(a, b)
    s = min(a, b)
    for i in range(g, a * b + 1, g):
        if i % s ==  0:
            return i

a = 45
b = 76
print(lcm(a, b))      