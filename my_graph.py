import copy
class my_graph:

    def __init__(self,vertices = None,edges = None, directed = True):
        """edges must be dictionary, vertices must be set"""
        self.directed = directed
        if vertices == None:
            self.vertices = set()
        else :
            self.vertices = vertices
            self.edges = {}
            for vertice in vertices:
                self.edges.update({vertice:[]})

        if edges == None and vertices == None:
            self.edges = {}
        else:
            temp_edges = {}
            for edge in edges:
                if edge not in self.edges:
                    self.edges.update(edge)
                else:
                    self.edges[edge] = edges[edge]
            if not self.directed:
                for self_edge in self.edges:
                    for element in self.edges[self_edge]:
                        if element not in self.edges:
                            temp_edges.update({element:[self_edge]})
                        else:
                            self.edges.update(temp_edges)
                            temp_edges = {}
                            if self_edge not in self.edges[element]:
                                self.edges[element].append(self_edge)
            #seems to work but just try with another model ;)
    def add_vertices(self,vertices):
        for vertice in vertices:
            if vertice not in self.vertices:
                self.vertices.add(vertice)
                self.edges.update({vertice:[]})

    def add_edges(self,edges):
        for key in edges:
            if key not in self.vertices:
                self.vertices.add(key)
                self.edges.update({key:edges[key]})
                if not self.directed:
                    for element in edges[key]:
                        if element in self.edges:
                            self.edges[element].append(key)
                        else:
                            self.vertices.add(element)
                            self.edges.update({edges[key]:key})
            else:
                for element in edges[key]:
                    self.edges[key].append(element)
                    if not self.directed:
                        for element in edges[key]:
                            if element in self.edges:
                                self.edges[element].append(key)
                            else:
                                self.vertices.add(element)
                                self.edges.update({edges[key]:key})
