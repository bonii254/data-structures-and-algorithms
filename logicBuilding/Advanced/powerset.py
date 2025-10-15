def powerSet(n):
    l = len(n)
    result = []
    for i in range(1 << l):
        subset = ""
        for j in range(l):
            if i & (1 << j):
                subset += n[j]
        result.append(subset)
    return result
        
print(powerSet("abc"))