# write a python program to perform addition and substraction of two matrices and display the elements of the resultant matrix

def matrix_operations(matrix1, matrix2):
    
    # Initialize the resulting matrices
    addition_result = []
    subtraction_result = []
    
    # Perform row-wise addition and subtraction
    for i in range(len(matrix1)):
        rem1 = matrix1[i]
        rem2 = matrix2[i]
        addition_row = []
        subtraction_row = []
    
        for j in range(len(rem2)):# or len(rem1)
            addition_row.append(rem1[j] + rem2[j])
            subtraction_row.append(rem1[j] - rem2[j])
        
        addition_result.append(addition_row)
        subtraction_result.append(subtraction_row)
    
    return addition_result, subtraction_result


# Get input from the user for matrix dimensions
row1 = int(input("Enter the number of rows for matrix1: "))#2
col1 = int(input("Enter the number of columns for matrix1: "))#2
row2 = int(input("Enter the number of rows for matrix2: "))#2
col2 = int(input("Enter the number of columns for matrix2: "))#2
# Check if matrices have the same number of rows
if (row1 != row2 and col1 != col2) or (row1 == 0):
    print("Error:Both Matrices have unequal number of rows and columns, so addition and substraction of two matrices can not possible here.")
else:
   # Get input for matrix elements
   print("Enter elements for the first matrix:")
   matrix1 = [[int(input("Enter element at position ({},{}) : ".format(i+1, j+1))) for j in range(col1)] for i in range(row1)]

   print("Enter elements for the second matrix:")
   matrix2 = [[int(input("Enter element at position ({},{}) : ".format(i+1, j+1))) for j in range(col2)] for i in range(row2)]

   # Perform row-wise addition and subtraction
   result_addition, result_subtraction = matrix_operations(matrix1, matrix2)

   # Print the result
   print("Addition Result:")
   for row in result_addition:
       print(row)

   print("Subtraction Result:")
   for column in result_subtraction:
       print(column)