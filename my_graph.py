import copy
class my_graph:

    def __init__(self,vertices = None,edges = None, directed = True):
        """edges must be dictionary, vertices must be set"""
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
            if not directed:
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
        pass
        '''self.vertices.add(vertices)
        if (vertices not in self.edges.keys()):
            self.edges.update({vertices:[]})'''

    def add_edges(self,edges):
        pass

        '''new_edges = copy.deepcopy(edges)
        for edge in edges:
            for value in edges[edge]:
                new_edges.update({value:edges[edge].append(edge)})'''
