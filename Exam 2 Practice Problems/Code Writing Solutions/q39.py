import numpy as np

def matrix_mult(mat1, mat2):
    """ Calculates the cross product of the two matrices if possible"""

    inner_mat1 = mat1.shape[1]
    inner_mat2 = mat2.shape[0]

    # Return empty array if not matching
    if inner_mat1 != inner_mat2:
        return np.array([])
    
    else:
        return np.matmul(mat1, mat2)  # Equivalent to return mat1 @ mat2
    

A = np.array([[0, 1], [2, 3]])
B = np.array([[ 0,  1,  2,  3], [ 4,  5,  6,  7] ,[ 8,  9, 10, 11]])

print(matrix_mult(A, B))