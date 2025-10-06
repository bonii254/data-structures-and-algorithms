def rectangleOverlap(x1, y1, x2, y2, a1, b1, a2, b2):
    if x2 < a1 or a2 < x1 or y2 < b1 or b2 < y1:
        return False
    return True

print(rectangleOverlap(0, 0, 2, 2, 1, 1, 3, 3))
print(rectangleOverlap(0, 0, 1, 1, 2, 2, 3, 3))