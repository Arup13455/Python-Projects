str = "ARUP"
print_A = [[" "for i in range(5)]for j in range(6)]# i = cols , j = rows
print_R = [[" "for i in range(5)]for j in range(6)]
print_U = [[" "for i in range(5)]for j in range(6)]
print_P = [[" "for i in range(5)]for j in range(6)]
#  code for A
for row in range(6):
    for col in range(5):
        if ((col==0 or col == 4) and row != 0) or ((row == 0 or row == 3) and (0<col<4)):
            print_A[row][col] = "*"
# code for R
for row in range(6):
    for col in range(5):
        if((col == 0 or row == 0 or row == 3) and col != 4) or (col == 4 and(0<row<3)) or ((row == col + 3) and 0<col<3):
            print_R[row][col] = "*"
# code for U
for row in range(6):
    for col in range(5):
        if ((col == 0 or col == 4) and row != 5) or (row == 5 and (0<col<4)):
            print_U[row][col] = "*"
# code for P
for row in range(6):
    for col in range(5):
        if ((col == 0 or row == 0) and col != 4) or (col == 4 and 0<row<2) or (row == 2 and (col == 3)) or (row == 3 and (0<col<3)):
            print_P[row][col] = "*"
# printing the result
for i in range(6):
    for j in range(5):
        print(print_A[i][j],end = " ")
    print(end = "  ")
    for j in range(5):
        print(print_R[i][j],end = " ")
    print(end = "  ")
    for j in range(5):
        print(print_U[i][j],end = " ")
    print(end = "  ")
    for j in range(5):
        print(print_P[i][j],end = " ")
    print()
