
#YET TO BE DONE
def gaussian_elimination(M):
    n=len(M)
    print(n)

    for i in range(0,n-1):
        d=M[i,i]
        for j in range(i+1,n):
            ele=M[j,i] #elements of col i, below the diagonal
            # print(M[j,:])
            if(d!=0):
                M[j,:]=M[j,:]-(ele/d)*M[i,:]
    return M