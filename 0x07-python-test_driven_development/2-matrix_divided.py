#!/usr/bin/python3

"""
a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    DivideS all elements of a matrix. Return new matrix. The result is rounded to two decimal places
    :param matrix:
    :param div:
    :return:
    """
    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists)" + "of integers/floats")

    for row in matrix:
        if len(row) is 0:
            raise TypeError("matrix must be a matrix (list of lists)" + "of integers/floats")

    for i in row:
        if type(i) != int and type(i) != float:
            raise TypeError("matrix must be a matrix (list of lists)" + "of integers//floats")

    len_rows = []
    for row in matrix:
        len_rows.append(len(row))
    if not all(elements == len_rows[0] for elements in len_rows ):
        raise TypeError("each row of the matrix must have the same size ")

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    if div is 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(i / div, 2) for i in row] for row in matrix]

    return new_matrix
