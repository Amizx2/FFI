#Task I need a wristband. Help me in identifying an actual wristband. A wristband can have 4 patterns: horizontal: each item in a row is identical. vertical: each item in each column is identical. diagonal left: each item is identical to the one on it's upper left or bottom right. diagonal right: each item is identical to the one on it's upper right or bottom left. Write a function that returns True if the section can be correctly classified into one of the 4 types, and False otherwise.
def wristband(matrix):
    Flag_horizontal = True
    Flag_vertical = True
    Flag_diagonal_left = True
    Flag_diagonal_right = True
    for row in matrix:
        if len(set(row)) != 1:
            Flag_horizontal = False
            break
    for j in range(len(matrix[0])):
        if len(set(row[j] for row in matrix)) != 1:
            Flag_vertical = False
            break
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] != matrix[i - 1][j - 1]:
                Flag_diagonal_left = False
                break
    for i in range(1, len(matrix)):
        for j in range(len(matrix[0]) - 1):
            if matrix[i][j] != matrix[i - 1][j + 1]:
                Flag_diagonal_right = False
                break
    return Flag_horizontal or Flag_vertical or Flag_diagonal_left or Flag_diagonal_right
print(wristband([["A", "A"], ["B", "B"], ["C", "C"]]))
print(wristband([["A", "B"], ["A", "B"], ["A", "B"]]))
print(wristband([["A", "B", "C"], ["C", "A", "B"], ["B", "C", "A"], ["A", "B", "C"]]))
print(wristband([["A", "B", "C"], ["B", "C", "A"], ["C", "A", "B"], ["A", "B", "A"]]))