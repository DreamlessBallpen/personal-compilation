
class Vertex:
	def __init__(
        self, 
        vertex_id, 
        label_name=None, 
        metadata=None
    ):
        self.id = vertex_id,
        self.label_name = label or str(vertex_id)
        self.metadata = metadata or {}