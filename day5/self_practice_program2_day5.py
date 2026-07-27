def matrix_maker(matrix_number):
    rows = int(input(f"Enter the number of rows for Matrix {matrix_number}: "))
    cols = int(input(f"Enter the number of columns for Matrix {matrix_number}: "))

    matrix = []

    print(f"Enter Matrix {matrix_number}:")

    for i in range(rows):
        row = []
        for j in range(cols):
            num = int(input(f"Enter element [{i}][{j}]: "))
            row.append(num)
        matrix.append(row)

    return matrix


def print_matrix(matrix, title):
    print(title)
    for row in matrix:
        print(row)


def matrix_multiply(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])

    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    if cols1 != rows2:
        print("Matrix multiplication is not possible.")
        return None

    result = [[0] * cols2 for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result


matrix1 = matrix_maker(1)
matrix2 = matrix_maker(2)

print_matrix(matrix1, "First Matrix:")
print_matrix(matrix2, "Second Matrix:")

result = matrix_multiply(matrix1, matrix2)

if result is not None:
    print_matrix(result, "Resultant Matrix:")