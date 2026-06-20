
class Edge:
    def __init__(
        self,
        source,
        target,
        weight=1,
        directed=True,
        metadata=None
    ):
        self.source = source
        self.target = target
        self.weight = weight
        self.directed = directed,
        self.metadata = metadata or {}