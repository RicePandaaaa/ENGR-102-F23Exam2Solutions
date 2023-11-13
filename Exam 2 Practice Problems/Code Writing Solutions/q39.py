import numpy as np

def matmultiply(A, B):
    """ Multiply matrices A and B if valid """
    inner_A = A.shape[1]
    inner_B = B.shape[0]

    # If the inner dimensions don't match
    if inner_A != inner_B:
        return np.array([])
    
    # If the inner dimensions do match
    else:
        return np.matmul(A, B)
