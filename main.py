from generateG import GraphGenerator, DrawGraph
from laplacianM import GenerateLaplacianMatrix
from determinantML import DetOfTransformedMatrix

nodes = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]
# nodes = [65, 66, 67]
G = GraphGenerator(nodes)
DrawGraph(G)

L = GenerateLaplacianMatrix(G)
print("Laplacian Matrix")
print(L)

# LEFT TO DO
# Transform The minor of Laplacian matrix to Augmented form(upper triangular) HERE 
ML = L  # for now, for testing below function

# Det of Transformed Matrix
det_of_L_minor = DetOfTransformedMatrix(ML)
print("No. of Spanning Tree for this graph is: ", det_of_L_minor)
