

class Graph:
    def __init__(
        self, 
        error_on_redundant_items,
        overwrite_redundant,
    ):
        self.adj = {}
        self.error_on_redundant_items = error_on_redundant_items
        self.overwrite_redundant = overwrite_redundant
        
    
    def add_vertex(self, v):
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
        