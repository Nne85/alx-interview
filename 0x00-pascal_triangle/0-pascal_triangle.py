#!/usr/bin/env python3

def pascal_triangle(n):
    """ This function generates a Pascal's Triangle up to nth level
    Args:
        n (int): The number of levels in the Pascal Triangle
    Returns:
        list[list[int]]: A list of lists representing Pascal's triangle
    """
    if (n <= 0):
        return []

    p_triangle = [[1]]

    for i in range(1, n):
        row =[1]
        for j in range(1, i):
            row.append(p_triangle[i - 1][j - 1] + p_triangle[i - 1][j])
        row.append(1)
        p_triangle.append(row)

    return p_triangle
