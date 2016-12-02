class Vertex: #the vertex class#
    def __init__(self, n): # list hold the neighbors, and the node is equal to n#
        self.name=n
        self.neighbors=list()
        
    def add_neighbor(self, v): # the function to add neighbors, it checks that if v is not in self. neighbors, if it is it appends it then sort it#
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()

    def getId(self): 
        return self.name
    
    def get_connections(self): #tmethod returns all of the vertices in the adjacency list#
        return self.neighbors.keys()

            
class Graph:
    def __init__(self):        
        self.vertices={} #the vertices list that holds the ke value pairs of vertices and their neighbors#

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name]=vertex
            return True
        else:
            return False
#checks to see if the instances of vertex and vertex is not in the list, then returns true#
    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices: #checks to see if u and v key value pairs are in the verties list and then rturn true or false#
            for key, value in self.vertices.items():
                if key==u:
                    value.add_neighbor(v)
                if key==v:
                    value.add_neighbor(u)
            return True
        else:
            return False
    
    def get_neighbors(self): # for each key(vertex) prints the values(neighbors)#
        for i in self.vertices.keys():
            print(i,self.vertices[i].neighbors)

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key,str(self.vertices[key].neighbors))

    def depth_first_search(self, v):
        s=[]
        visited=[]
        s.append(v)
        while s != []:
            u=s.pop()
            if u not in visited:
                visited.append(u)
                for edges in range(len(self.vertices[u].neighbors)):
                    n=self.vertices[u].neighbors[edges-1]
                    s.append(n)
        return visited
        
    def breadth_first_search(self, v):
        q=[]
        visited=[]
        q.insert(0,v)
        while q != []:
            u=q.pop()
            if u not in visited:
                visited.append(u)
            for edges in range(len(self.vertices[u].neighbors)):
                n=self.vertices[u].neighbors[edges-1]
                if  n not in visited:
                    q.insert(0,n)
        return visited
        
g=Graph()

for i in range(6):
    g.add_vertex(Vertex(i))
g.vertices

g.add_edge(0,1)
g.add_edge(0,5)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(3,4)
g.add_edge(3,5)
g.add_edge(4,0)
g.add_edge(5,4)
g.add_edge(5,2)


g.get_neighbors()
print(g.depth_first_search(0))
print(g.breadth_first_search(0))
