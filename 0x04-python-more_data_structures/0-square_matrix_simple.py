#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
temp_matrix = []
for x in matrix:
temp_matrix.append(list(map(lambda x: x**2, x)))
return (temp_matrix)
