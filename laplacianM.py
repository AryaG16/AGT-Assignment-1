import numpy as np 


def GenerateLaplacianMatrix(G):
    num_v = len(G.nodes)  # matrix of 11 X 11
    # print(num_v)
    L = np.zeros((num_v, num_v))

    for i in G.nodes:
        connected_nodes = list(G.neighbors(i))
        degree = len(connected_nodes)
        
        # print(i)
        i = ord(i) - 65
        # setting diagonal of Laplacian-L
        L[i][i] = degree

        for j in connected_nodes:
            j = ord(j) - 65
            L[i][j] = -1
            
    return L
