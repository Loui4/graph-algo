class Graph:

    def __init__(self) -> None:
        self.nodes = []
        self.graph = [[0 for _ in range(9)] for _ in range(9)]
     
    
    def add_node(self,node_name):
        self.nodes.append(node_name)
        index = self.nodes.index(node_name)
        self.graph[index][index]=0
    
    def add_edge(self, node_one, node_two, weight):

        if node_one in self.nodes and node_two in self.nodes:
            print("exists")
            indexOne = self.nodes.index(node_one)
            indexTwo = self.nodes.index(node_two)

            self.graph[indexOne][indexTwo]= weight
        else:
            print("nodes doesn't exist")




districts = ["Nkhotakota","Salima","Ntcheu","Dedza","Lilongwe","Mchinji","Kasungu","Ntchisi","Dowa"]
graph =Graph()

for district in districts:
    graph.add_node(district)


graph.add_edge(districts[0],districts[1],112)
graph.add_edge(districts[0],districts[7],66)
graph.add_edge(districts[1],districts[8],67)
graph.add_edge(districts[1],districts[3],96)
graph.add_edge(districts[2],districts[3],74)
graph.add_edge(districts[3],districts[4],92)
graph.add_edge(districts[4],districts[8],55)
graph.add_edge(districts[4],districts[5],109)
graph.add_edge(districts[5],districts[6],141)
graph.add_edge(districts[6],districts[7],66)
graph.add_edge(districts[6],districts[8],117)
graph.add_edge(districts[7],districts[8],38)

graph.add_edge(districts[1],districts[0],112)
graph.add_edge(districts[7],districts[0],66)
graph.add_edge(districts[8],districts[1],67)
graph.add_edge(districts[3],districts[1],96)
graph.add_edge(districts[3],districts[2],74)
graph.add_edge(districts[4],districts[3],92)
graph.add_edge(districts[8],districts[4],55)
graph.add_edge(districts[5],districts[4],109)
graph.add_edge(districts[6],districts[5],141)
graph.add_edge(districts[7],districts[6],66)
graph.add_edge(districts[8],districts[6],117)
graph.add_edge(districts[8],districts[7],38)



for row in graph.graph:
    for element in row:
        print(element, end=" ")
    print()

