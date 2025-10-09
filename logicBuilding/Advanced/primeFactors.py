import math
"""Space complexity: O(1) time complexity O(√n)"""


def primeFactors(num):
    factors = []
    
    while num % 2 == 0:
        if 2 not in factors:
            factors.append(2)
        num //= 2
        
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            if i not in factors:
                factors.append(i)
            num //= i
            
    if num > 2:
        factors.append(num)
        
    return factors

num = 84
print(f"Prime factors of {num} are: {primeFactors(num)}")