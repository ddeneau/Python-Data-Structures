import random
# Given a square matrix, count the number of steps it takes to reach
# the bottom right corner starting from the top left corner.


# Solution will be computed recursively using the following function
# matrix - The matrix in question.
# row - The current row in the traversal.
# column - The current column in the traversal.
# rows - The TOTAL number of rows in the matrix.
# columns - The TOTAL number of columns in the matrix.
# path - A list storing the steps in the traversal.
# path_index - Index of the path.
def find_steps_in_path(matrix, row, column, rows, columns, count, index):
    # First check for two special locations this function can be called for:
    # The top right corner, [column = columns - 1] (can only go downwards to the goal)
    # The bottom left corner, [row = rows - 1] (can only go right towards the goal)
    if column == columns - 1:
        return

    if row == rows - 1:
        return

    # Add to our counter list the row and column we'll traverse next.
    count.append(row)
    count.append(column)

    # Call the same function, traversing one row and one column over.
    find_steps_in_path(matrix, row + 1, column + 1, rows, columns, count, index + 1)


def sum_rows(arr, m, n, i, j, sum):
    if i == m - 1 or j == n - 1:
        return sum

    sum += arr[i][j]



def run_matrix_path_problem(m, n):
    number_of_rows = m
    number_of_columns = n
    array_2d = [[0] * number_of_rows] * number_of_columns
    steps = list()
    print("Array: \n")
    array = ""

    for i in range(0, number_of_columns):
        for j in range(0, number_of_rows):
            number = random.randrange(1, 9)
            array_2d[i][j] = number
            array += "[" + str(number) + "]"
        array += "\n"

    print(array)
    print("DONE.")
    print("Steps: " + str(find_steps_in_path(array_2d, 0, 0, number_of_rows, number_of_columns, steps, 0)))
    print(str(len(steps)))


run_matrix_path_problem(2, 2)
run_matrix_path_problem(3, 3)
run_matrix_path_problem(4, 4)
run_matrix_path_problem(5, 5)

run_matrix_path_problem(20, 21)





