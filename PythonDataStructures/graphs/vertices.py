
class Vertex:
    def __init__(
        self, 
        vertex_id, 
        label_name=None, 
        metadata=None
    ):
        self.id = vertex_id
        self.label_name = label_name or str(vertex_id)
        self.metadata = metadata or {}
        
    def __hash__(self):
        return hash((self.id, self.label_name))
        
    def __eq__(self, other):
        return self.id == other.id and self.label_name == other.label_name
        
    def is_hashable(self):
        return True
        
    def __str__(self):
        
        display_name = self.id if self.label_name is None else self.label_name
        return f"{display_name}"
    
    def deepcopy(self):
        # TODO: Implement a way to handle this for when metadata has nested structures.
        # This is a shallow copy for now, but vertex_id and label_name are immutable. I think.
        return Vertex(self.id, label_name=self.label_name)
    

   