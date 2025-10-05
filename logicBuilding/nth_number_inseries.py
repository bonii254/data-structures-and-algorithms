"""using loop WITH TIME COMPLEXITY OF O(n) and space complexity of O(1)"""


def nthNumberLoop(number):
    ans = 0
    for i in range(1, number + 1):
        ans = ans + i
        
    return ans


"""using formula time and space complexity O(1)"""


def nthNumberFormula(number):
    return abs(number * (number + 1) / 2)


print (nthNumberLoop(4))
print (nthNumberFormula(4))