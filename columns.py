def top_column(matrix):
    rows = len(matrix)
    col = len(matrix[0])

    max_sum = None
    max_col_index = 0

    for column in range(col):
        sum_of_column = 0

        for row in range(rows):
            sum_of_column += matrix[row][column]

        if max_sum is None or sum_of_column > max_sum:
            max_sum = sum_of_column
            max_col_index = column

    return max_col_index        

# Test cases
matrix_1 = ((5, 6, 7, 8),
            (3, 9, 2, 5),
            (2, 1, 9, 2))
assert top_column(matrix_1) == 2

matrix_2 = ((1, 2),
            (3, 4))
assert top_column(matrix_2) == 1

matrix_3 = ((3,),
            (4,),
            (9,))
assert top_column(matrix_3) == 0

matrix_4 = ((-2, -1, -3),)
assert top_column(matrix_4) == 1

print("All tests passed!")
print("Finished early? Discuss time & space complexity")



# I will make a tuple of each column separately

# using index I will iterate through each column in matrix

# I will add all the numbers which are in that column

# Identifying highest sum - I will compare all colum sum values , get the highest value - return that column index value