# Write a Python program to read and print a (n * m) matrix using for loop 
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

matrix = []
print("Enter the entries rowwise:")

for i in range(R):      
    a =[]
    for j in range(C):     
         a.append(int(input()))
    matrix.append(a)
  
# For printing the matrix
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end = " ")
    print()