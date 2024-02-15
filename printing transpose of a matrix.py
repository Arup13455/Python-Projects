# Write a python program to transpose a matrix
rows = int(input("Enter a num for rows: "))
cols =	int(input("Enter a num for columns: "))
# Get input for the matrices
print("Enter elements for the matrix:")
matrix = [[int(input("Enter element at position ({},{}) : ".format(i+1, j+1))) for j in range(cols)] for i in range(rows)]
# transposing the matrix
trans = [[0 for i in range(rows)]for j in range(cols)]
for i in range(rows):
	for j in range(cols):
		trans[j][i] = matrix[i][j]
	
# printing the transposed matrix
print("Transpose Matrix's elements are: ")
for m in trans:
	print(m)