import random


class Node:
    def __init__(self, name):
        self.name=name
        self.neighbors=[]
        self.degree=0
    
    def add_neighbor(self,n):
        self.neighbors.append(n)
        self.degree +=1
        

# Graph Creation
def GraphGenerator(nodes):

    nodeList={}
    for a in nodes:
        node=Node(chr(a))
        nodeList.update({chr(a):node})
    
    for p in nodeList:
        print("node: ",nodeList[p].name)
        print("   Neighbors: ",nodeList[p].neighbors)
        print("   Degree: ",nodeList[p].degree)
        

    print("\n")

    # Edges
    for alpha in nodes:
        for beta in nodes:
            if(alpha >= beta):
                continue
            a=chr(alpha)
            b=chr(beta)
            node1=nodeList[a]
            node2=nodeList[b]

            add_prob = random.randint(0, 1)
            if add_prob == 1:
                node1.add_neighbor(b)
                node2.add_neighbor(a)

    for p in nodeList:
        print("node: ",nodeList[p].name)
        print("   Neighbors: ",nodeList[p].neighbors)
        print("   Degree: ",nodeList[p].degree)
    
    print("\n")

    return nodeList


