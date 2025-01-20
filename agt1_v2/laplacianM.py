def GenerateLaplacianMatrix(nodeList):
    more_component=0
    num_v = len(nodeList) 

    L=[[0 for _ in range(num_v)] for _ in range(num_v)]

    for i in nodeList: #i is a key of dict

        connected_nodes = nodeList[i].neighbors
        degree = nodeList[i].degree
        
        idx = ord(i) - 65
        # setting diagonal of Laplacian-L
        L[idx][idx] = degree

        for j in connected_nodes:
            j = ord(j) - 65
            L[idx][j] = -1
            
    return L, more_component