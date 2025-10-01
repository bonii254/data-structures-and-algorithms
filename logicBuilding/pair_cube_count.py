def count_pairs(n):
    count = 0
    values = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i**3 + j**3 == n:
                count += 1
                values.append((i, j))
    return f"count is {count} and values are{values}"

print(count_pairs(35))