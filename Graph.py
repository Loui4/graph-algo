class Graph:

    def __init__(self) -> None:
        self.nodes = []
        self.graph = [[0 for _ in range(9)] for _ in range(9)]
     
    
    def add_node(self,node_name):
        self.nodes.append(node_name)
        index = self.nodes.index(node_name)
        self.graph[index][index]=0
    

graph =Graph()
graph.add_node("hey")
graph.add_node("hello");


print(graph.graph)
