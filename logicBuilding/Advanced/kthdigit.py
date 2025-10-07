def kth_digit_from_right(a, b, k):
    """
    Return the k-th digit from right in a^b.
    """
    n = a ** b
    s = str(n)
    if k > len(s):
        return None  
    return int(s[-k])

    
a = 5
b = 2
k = 1
print(kth_digit_from_right(a, b, k))