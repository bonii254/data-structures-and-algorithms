import math


def finddistance(x1, x2, y1, y2):
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2-y1, 2))


print(finddistance(7, 3, 7, 4))