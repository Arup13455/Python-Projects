row1 = int(input("Enter the number of rows for matrix1: "))
col1 = int(input("Enter the number of columns for matrix1: "))
row2 = int(input("Enter the number of rows for matrix2: "))
col2 = int(input("Enter the number of columns for matrix2: "))
if col1 != row2:
    print("Matrix multiplication is not possible here.")
else:
    # Get input for the matrices
    print("Enter elements for the first matrix:")
    matrix1 = [[int(input("Enter element at position ({},{}) : ".format(i+1, j+1))) for j in range(col1)] for i in range(row1)]
    print("Enter elements for the second matrix:")
    matrix2 = [[int(input("Enter element at position ({},{}) : ".format(i+1, j+1))) for j in range(col2)] for i in range(row2)]
    multiply_result = [[0 for i in range(col2)] for j in range(row1)]
    for i in range(row1):
        for j in range(col2):
            for k in range(col1):
                multiply_result[i][j] += matrix1[i][k] * matrix2[k][j]
    print("Multiplied matrix: ")
    for l in multiply_result:
        print(l)