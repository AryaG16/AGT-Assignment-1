from generateG import GraphGenerator #DrawGraph
from laplacianM import GenerateLaplacianMatrix
from determinantML import DetOfTransformedMatrix
from gaussianE import gaussian_elimination

# Generating Random Graph of 11 nodes
nodes = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]
nodes = [65, 66, 67,68]
nodeList = GraphGenerator(nodes)


# Making the Laplacian Matrix
L,mc = GenerateLaplacianMatrix(nodeList)
print(">>> Laplacian Matrix")
for row in L:
    print(row)
print(" Order of Laplacian's Matrix: ", len(L),"X",len(L[0]))
print("\n")


# Getting Minor Matrix of Laplacian
ML = [row[:-1] for row in L[:-1]]
print(">>> Minor Matrix of Laplacian's")
for row in ML:
    print(row)
print(" Order of the Minor Matrix : ", len(ML),"X",len(ML[0]))
print("\n")


# Getting Upper Triangular Matrix using gaussian elimination
UTM = gaussian_elimination(ML)  
print(">>> Upper Triangular Matrix")
for row in UTM:
    print(row)
print(" Order of the UTM Matrix : ", len(UTM),"X",len(UTM[0]))
print("\n")


# # Det of Upper Triangular Matrix
det_of_L_minor = DetOfTransformedMatrix(UTM)
print("No. of Spanning Tree for this graph is: ", det_of_L_minor+mc)

