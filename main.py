from generateG import GraphGenerator, DrawGraph
from laplacianM import GenerateLaplacianMatrix
from determinantML import DetOfTransformedMatrix
from gaussianE import gaussian_elimination

# Generating Random Graph of 11 nodes
nodes = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]
# nodes = [65, 66, 67]
G = GraphGenerator(nodes)
DrawGraph(G)

# Making the Laplacian Matrix
L = GenerateLaplacianMatrix(G)
print("Laplacian Matrix")
print(L)

# Getting Minor Matrix of Laplacian
n=len(L)
print(" Order of Laplacian's Matrix: ", L.shape)
ML=L[:n-1,:n-1]
print(" Order of the Minor Matrix of Laplacian's Matrix: ", ML.shape)
print("Minor Matrix of Laplacian's")
print(ML)

# Getting Upper Triangular Matrix using gaussian elimination
UTM = gaussian_elimination(ML)  

# Det of Upper Triangular Matrix
# det_of_L_minor = DetOfTransformedMatrix(UTM)
# print("No. of Spanning Tree for this graph is: ", det_of_L_minor)
