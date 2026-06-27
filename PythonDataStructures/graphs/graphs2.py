
print("Importing the vertices module...")
from vertices import Vertex
print("Done importing the vertices module! (If not done before)")


class Graph:
    def __init__(
        self, 
        error_on_redundant_items=True,
        overwrite_redundant=False,
    ):
        self.adj = {}
        self.vertex_id_to_label_map = dict()
        self.error_on_redundant_items = error_on_redundant_items
        self.overwrite_redundant = overwrite_redundant
        
    
    def add_vertex(self, v:Vertex):
        """ Vertices are implemented to be hashable here. """
        
        # Let's take the elements already in adj into consideration as well.
        if len(self.adj) == 0:
            print(f"[DEBUG_PRINT]: No elements yet, adding vertex {v} immediately")
            self.adj[v] = {}
            return
        
        # Case 1: Error on redundant items is True and it is redundant.
        if self.error_on_redundant_items and (v in self.adj):
            raise ValueError(f"Function <<add_vertex>> failed. | Vertex {v} already exists. | Error on redundant items: {self.error_on_redundant_items}")
        # Case 2: Error on redundant items is False and it is redundant.
        elif not(self.error_on_redundant_items) and (v in self.adj):
            # Case 2-1: No error, just ignore.
            if not(self.overwrite_redundant):
                return
            # Case 2-2: Overwrite. Put a warning.
            else:
                print(f"[WARNING]: Vertex {v} will be overwritten to contain a blank dictionary of elements. | overwrite_redundant: {self.overwrite_redundant}")
                # [TODO]: Implement code to remove v's edges as well.
                self.adj[v] = {}
        # Case 3: Whether error on redundant items is true or false, the vertex we have right now is unique anyway.
        elif not(v in self.adj):
            # Just like Case 2-2, but no warning this time.
            self.adj[v] = {}
        else:
            raise Exception(f"[TODO]: Programming error. There's a branch you haven't thought of yet")


def run_tests():
    print("[TEST]: Creating a graph, with default behavioral parameters...")
    graph1 = Graph()
    print("Created a graph!")
    print("[TEST]: Creating a graph, with error on redundant items = True, overwrite_redundant = True")
    graph2 = Graph(error_on_redundant_items=True, overwrite_redundant=True)
    print("Created a graph!")
    print("[TEST]: Creating a graph, with error on redundant items = True, overwrite_redundant = False")
    graph3 = Graph(error_on_redundant_items=True, overwrite_redundant=False)
    print("Created a graph!")
    print("[TEST]: Creating a graph, with error on redundant items = False, overwrite_redundant = True")
    graph4 = Graph(error_on_redundant_items=False, overwrite_redundant=True)
    print("Created a graph!")
    print("[TEST]: Creating a graph, with error on redundant items = False, overwrite_redundant = False")
    graph5 = Graph(error_on_redundant_items=False, overwrite_redundant=False)
    print("Created a graph!")
    
    print()
    
    print("Creating a vertex: vertex_id: 'A', label_name: 'First'")
    a = Vertex(vertex_id="A", label_name="First")
    print("Done creating the first vertex!")
    
    print("\n", a, "\n")
    
    graphs = {
        "graph1": graph1,
        "graph2": graph2,
        "graph3": graph3,
        "graph4": graph4,
        "graph5": graph5
    }
    
    print("[TEST]: Testing the add_vertex function to all graphs created: Since there are no elements yet, all should just add the vertex, no question")
    for g_name, g in graphs.items():
        g.add_vertex(a.deepcopy())
        print("Done adding the vertex!")
        
    print("[PRINT]: Printing the first vertex in all graphs' self.adj dictionary. This can be done in Python 3.7+ and later.")
    for g_name, g in graphs.items():
        print("[REMOVE_DEBUG]: Checking the adj values in current graph")
        print(g.adj)
        print(f"graph_name: {g_name} | graph_first_element: {list(g.adj)[0]}")
    print("Done printing all of the first elements!")
    
    print("[TEST]: Testing the 

if __name__ == "__main__":
    run_tests()