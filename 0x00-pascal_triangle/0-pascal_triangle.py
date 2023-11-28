#!/usr/bin/env python3
"""interview question on Pascal's Triangle"""


def pascal_triangle(n):
    """ This function generates a Pascal's Triangle up to nth level
    Args:
        n (int): The number of levels in the Pascal Triangle
    Returns:
        list[list[int]]: A list of lists representing Pascal's triangle
    """

    if (n <= 0):
        return []

    pascalTriangle = []

    for i in range(n):
        # Initialize the first row of Pascal's triangle if necessary
        if i == 0:
            pascalTriangle.append([1])
        else:
            row = pascalTriangle[i - 1]
            currentRow = [1]
            for j in range(1, len(row)):
                currentRow.append(row[j - 1] + row[j])
            currentRow.append(1)
            pascalTriangle.append(currentRow)

    return pascalTriangle
