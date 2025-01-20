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
    for a in range(nodes):
        node=Node(a)
        nodeList.update({a:node})
    
    for p in nodeList:
        print("node: ",nodeList[p].name)
        print("   Neighbors: ",nodeList[p].neighbors)
        print("   Degree: ",nodeList[p].degree)
        

    print("\n")

    # Edges
    for alpha in range(nodes):
        for beta in range(nodes):
            if(alpha >= beta):
                continue
            
            # a=chr(alpha)
            # b=chr(beta)
            node1=nodeList[alpha]
            node2=nodeList[beta]

            add_prob = random.randint(0, 1)
            if add_prob == 1:
                node1.add_neighbor(beta)
                node2.add_neighbor(alpha)

    for p in nodeList:
        print("node: ",nodeList[p].name)
        print("   Neighbors: ",nodeList[p].neighbors)
        print("   Degree: ",nodeList[p].degree)
    
    print("\n")

    return nodeList


