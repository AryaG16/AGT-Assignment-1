import numpy as np


# Function to find determinant of Augmented matrix(Upper triangular)
def DetOfTransformedMatrix(M):
    diagonals = np.diagonal(M)  # a list
    print("Diagonals", diagonals)

    determinant = 1
    for d in diagonals:
        determinant *= d

    return determinant
