class Graph:
        
    def __init__(self):
        self._nodes = {}
        self._edges = {}
    
    @property
    def node(self):
        return self._nodes
    
    @property
    def edge(self):
        veins = {}
        for x in self._edges:
            if x[0] not in veins:
                veins[x[0]] = {}
                
            veins[x[0]][x[1]] = self._edges[x]
            
        for x in self._nodes:
            if x not in veins:
                veins[x] = {}
        
        return veins
    
    def nodes(self):
        return list(self._nodes.keys())
    
    def edges(self):
        veins = []
        for x in self._edges.keys():
            if x[0] < x[1]:
                veins.append(x)
        return veins
    
    def add_node(self, node, attr_dict=None):
        if attr_dict == None:
            attr_dict = {}
            
        self._nodes[node]=attr_dict
    
    def add_edge(self, node1, node2, attr_dict=None):
        if node1 not in self._nodes:
            self.add_node(node1)
        if node2 not in self._nodes:
            self.add_node(node2)
            
        if attr_dict == None:
            attr_dict = {}
        else:
            attr_dict = dict(attr_dict.items())
            
        self._edges[(node1,node2)] = attr_dict
        self._edges[(node2,node1)] = attr_dict
    
    def add_nodes_from(self, node_list, attr_dict=None):
        if attr_dict == None:
            attr_dict = {}
            
        for x in node_list:
            b = dict(attr_dict.items())
            self.add_node(x,b)
    
    def add_edges_from(self, edge_list, attr_dict=None):
        if attr_dict == None:
            attr_dict = {}
            
        for x in edge_list:
            b = dict(attr_dict.items())
            self.add_edge(x[0],x[1],b)
    
    def degree(self, node):
        return len(list(self.edge[node].keys()))
    
    def __getitem__(self, node):
        return self.edge[node]
    
    def __len__(self):
        return len(self._nodes)
    
    def neighbors(self, node):
        return list(self.edge[node].keys())
    
    def remove_node(self, node1):
        if node1 in self._nodes:
            for x in self.edge[node1].keys():
                del self._edges[(node1,x)]
                del self._edges[(x,node1)]
                
            del self._nodes[node1]
    
    def remove_edge(self, node1, node2):
        if (node1, node2) in self._edges:
            del self._edges[(node1,node2)]
            del self._edges[(node2,node1)]
    
    def remove_nodes_from(self, node_list):
        for x in node_list:
            self.remove_node(x)
    
    def remove_edges_from(self, edge_list):
        for x in edge_list:
            self.remove_edge(x[0],x[1])
    
    def add_node_attribute(self, node, attr_name, value):
        self._nodes[node][attr_name] = value
    
    def add_edge_attribute(self, node1, node2, attr_name, value):
        self._edges[(node1,node2)][attr_name] = value
    
    def add_node_attribute_from(self, nodelist, attr_name, value):
        for x in nodelis:
            self.add_node_attribute(x, attr_name, value)
    
    def add_edge_attribute_from(self, edgelist, attr_name, value):
        for x in edgelist:
            self.add_node_attribute(x[0], x[1], attr_name, value)
    