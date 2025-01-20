def DetOfTransformedMatrix(M):
    determinant = 1
    for i in range(len(M)):
        for j in range(len(M)):
            if i==j:
                determinant *= M[i][j]
     
    return determinant
