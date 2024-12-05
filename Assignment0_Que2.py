import numpy as np
def accept_2d_array():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    array_data = []
    print("Enter the elements row by row:")
    for i in range(rows):
        row = input(f"Enter row {i + 1} (space-separated): ").split()
        array_data.append([float(x) for x in row])
    array = np.array(array_data)
    return array
print("We get data for first array")
if __name__ == "__main__":
    array_1=accept_2d_array()
print("We get data for second array")
if __name__ == "__main__":
    array_2=accept_2d_array()
def matrix_multiplication(x,y):
    rows1=len(x)
    rows2=len(y)
    cols1=len(x[0])
    cols2=len(y[0])
    if rows1!=cols2:
        raise ValueError('rows in x must be same to columns in y')
        print("rows in x ust be columns in y")
    result=[[0 for m in range(cols2)] for m in range(rows1)]
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j]+=x[i][k]*y[k][j]
    return result
def dot_product(k,l):
    if k.shape!=l.shape:
        raise ValueError('k and l must be same shape')
        print("k and l must be same shape")
    else:
        result=k*l
        return result

def get_minor(matrix,i,j):
    return [row[:j]+row[j+1:] for row in (matrix[:i]+matrix[i+1:])]
def determinant(matrix):
    n=len(matrix)
    if len(matrix[0])!=len(matrix):
        raise ValueError('matrix must be square matrix')
        print("matrix must be square matrix")
    else:
        if len(matrix) == 2 and len(matrix[0]) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        det=0
        for col in range(len(matrix)):
            minor=get_minor(matrix,0,col)
            cofactor=((-1)**col)*determinant(minor)*matrix[0][col]
            det+=cofactor

        return det









operation=input("what operation do you want to do? (DOT, MATRIX, DETERMINANT)")
if operation=="MATRIX":
       matrix=matrix_multiplication(array_1,array_2)
       print("The matrix_multiplication of the two arrays is: ")
       for row in matrix:
           print(row)
if operation=="DOT":
    dot=dot_product(array_1,array_2)
    print("The dot_product of the two arrays is: ")
    for row in dot:
        print(row)

if operation=="DETERMINANT":
    determinant_1=determinant(array_1)
    determinant_2=determinant(array_2)
    print(f"The determinant of array1 is: {determinant_1}\n The determinant of array2 is: {determinant_2}")




