def reversedigit(val):
    reversed = 0
    while val > 0:
        reversed = (reversed * 10) + (val % 10)
        val = val // 10
        
    return reversed

print(reversedigit(123456))