def findPrime(n):
    if n < 2:
        return []
    
    prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    res = []
    for p in range(2, n + 1):
        if prime[p]:
            res.append(p)
    
    return res


def sieve(n):
    if n < 2:
        return []
    
    prime = list(range(n + 1))
    
    for p in range(2, int(n ** 0.5 + 1)):
        if prime[p] != 0:
            for multiple in range(p * p, n + 1, p):
                prime[multiple] = 0
                
    prime = [x for x in prime if x != 0]
    return prime


print(sieve(50))