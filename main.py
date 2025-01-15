from generateG import GraphGenerator, DrawGraph
from laplacian import GenerateLaplacianMatrix

nodes = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]
G=GraphGenerator(nodes)
DrawGraph(G)

L=GenerateLaplacianMatrix(G)
print("Laplacian Matrix")
print(L)