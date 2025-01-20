def gaussian_elimination(M):
    n=len(M)
    print(n)

    for i in range(0,n-1):
        d=M[i][i]
        for j in range(i+1,n):
            ele=M[j][i] #elements of col i, below the diagonal
           
            if(d!=0):
                for e in range(n):
                    M[j][e]=M[j][e]-(ele/d)*M[i][e]
                    
    return M