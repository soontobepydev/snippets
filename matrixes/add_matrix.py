import numpy as np

#import numpy on your virtual environment

def add(matrix1, matrix2):
    matrix = [[0,0],[0,0]]

    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            matrix[i][j] = matrix1[i][j] + matrix2[i][j]
    return matrix

def add_python_way(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j]  for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def print_array(array):
    for line in array:
        print('  '.join(map(str, line)))

def main():
    matrix1 = np.array([[1, -2],[-3, 4]])
    matrix2 = np.array([[2, -1],[0, -1]])

    print('matrix1:')
    print_array(matrix1)
    print()

    print('matrix2:')
    print_array(matrix2)
    print()

    print('matrix 1 + matrix2:')
    print_array(add(matrix1, matrix2))
    print()

    print('matrix 1 + matrix2 with pythonic list compreehension:')
    print_array(add_python_way(matrix1, matrix2))

if __name__ == "__main__":
    main()
