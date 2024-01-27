row = int(input("Enter no. of rows: "))
column = int(input("Enter no. of columns: "))

matrix = []
print("Enter the elements in rowwise: ")

for i in range(row):
    a = []
    for j in range(column):
        a.append(int(input()))
    matrix.append(a)
    
print(matrix)

for i in range(row):
    for j in range(column):
        print(matrix[i][j],end=" ")
    print()