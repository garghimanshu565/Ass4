from collections import defaultdict
from queue import PriorityQueue
class Graph:
    def __init__(self, directed): 
        """Parametrized constructor of class Graph 
        which takes True if Graph is directed otherwise it takes False"""
        self.graph =  defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v, weight):
        """Add Edges between two nodes along 
        with Heuristic value as Algorithm is of Beam Search"""
        if self.directed:
            value = (weight, v)
            self.graph[u].append(value)
        else:
            value = (weight, v)
            self.graph[u].append(value)
            value = (weight, u)
            self.graph[v].append(value)

    def beam(self, current_node, goal_node,beamwidth):
        """It takes starting node and 
        goal node as parameters then it returns 
        a path using Beam Search Algorithm"""
        visited = []  
        queue = PriorityQueue()
        queue1 = PriorityQueue()
        queue.put((0, current_node))
        
        while not queue.empty():
            item = queue.get()
            current_node =  item[1]
            
            if current_node == goal_node:
                print(current_node, end = " ")
                queue.queue.clear()
            else:
                if current_node in visited:
                    continue
                    
                print(current_node, end = " ")
                visited.append(current_node)

                for neighbour in self.graph[current_node]:
                        queue.put((neighbour[0], neighbour[1]))
                for i in range(queue.qsize()):
                    it=queue.get()
                    if queue1.qsize()==beamwidth:
                        break
                    else:
                        queue1.put(it)
                queue.queue.clear()
                for i in range(queue1.qsize()):
                    it=queue1.get()
                    queue.put(it)
g = Graph(True)
g.graph =  defaultdict(list)
g.add_edge('A', 'B', 1)
g.add_edge('A', 'C', 3)
g.add_edge('B', 'D', 2)
g.add_edge('B', 'E', 2)
g.add_edge('C', 'F', 3)
g.add_edge('C', 'G', 0)

g.graph
g.beam('A', 'G',3)