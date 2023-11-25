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
        visited = set()
        return self._dfs(src, dst, visited)

    def _dfs(self, src: int, dst: int, visited: set) -> bool:
            if src == dst:
                return True
            visited.add(src)
            for neighbor in self.adj_list.get(src, []):
                if neighbor not in visited:
                    if self._dfs(neighbor, dst, visited):
                        return True
            return False   