import math
 
 
def getLargestPrime(num):
    largest_prime = -1
    
    while num % 2 == 0:
        largest_prime = 2
        num //= 2
        
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            largest_prime = i
            num //= i
    
    if num > 2:
        largest_prime = num
    
    return largest_prime



print(getLargestPrime(25))