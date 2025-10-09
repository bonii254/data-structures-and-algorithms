import math


def pascalsTriangle(num):
    triangle =[[1]]
    for i in range(1, num):
        prev_row = triangle[-1]
        curr_row = [1]
        for j in range(1, len(prev_row)):
            curr_row.append(prev_row[j - 1] + prev_row[j])
        curr_row.append(1)
        triangle.append(curr_row)
        
    length = len("  ".join(map(str, triangle[-1])))
    for row in triangle:
        row_str = "  ".join(map(str, row))
        print(row_str.center(length)) 


def pascal_triangle(n):
    for i in range(n):
        row = [math.comb(i, r) for r in range(i + 1)]
        print("  ".join(map(str, row)).center(n * 3))


pascalsTriangle(6)
pascal_triangle(6)