class Graph:
    def __init__(self):
        self.graph = {}
        self.vertices = set()
        self.edges = set()

    def addEdge(self, src: int, dst: int) -> None:
        self.vertices.add(src)
        self.vertices.add(dst)
        self.edges.add((src, dst))

    def removeEdge(self, src: int, dst: int) -> bool:
        if (src, dst) in self.edges:
            self.edges.remove((src, dst))
            return True
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        if src not in self.vertices or dst not in self.vertices:
            return False
        if src == dst:
            return True
        for edge in self.edges:
            if edge[0] == src:
                if self.hasPath(edge[1], dst):
                    return True
        return False