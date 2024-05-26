#!/usr/bin/python3
'''Module contains function pascal_triangle'''


def pascal_triangle(n):
    """
    Function returns Pascal's Triangle

    Args:
        n: Number of lines

    Returns:
        pt: Pascal's Triangle
    """

    pt = []
    for row in range(n):
        current_row = [1]
        if row > 0:
            prev = pt[-1]
            for i in range(len(prev) - 1):
                current_row.append(prev[i] + prev[i + 1])
            current_row.append(1)
        pt.append(current_row)
    return pt
