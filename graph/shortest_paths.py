from __future__ import annotations


# Helper Class to Display a given Path from A to Z properly
class Path(list[str]):
    def __repr__(self) -> str:
        return f"*{''.join(self)}"


# Helper Class to keep track of Shortest Paths excountered when going from A to Z.
# Can store multiple shortest paths
class ShortestPaths:
    def __init__(self):
        self.paths: list[Path] = []

    # Checks if a New Path to add is shorter than any previous ones
    # And adds depending on the case
    def check_add(self, path: list[str]):
        if self.length() > len(path):
            self.paths = [Path(path)]
        elif self.length() == len(path):
            self.paths.append(Path(path))

    # Joins paths from one to another
    def unchecked_consume(self, other: ShortestPaths):
        for other_path in other.paths:
            if other_path not in self.paths:
                self.paths.append(other_path)

    def length(self, default_length=float("inf")) -> float:
        # If there is no Path possible from A to Z then fallback to default length
        if len(self.paths) == 0:
            return default_length
        return len(self.paths[0])

    def __repr__(self) -> str:
        return repr(self.paths)

    # Unions consecutive paths such that 
    # if A -> Q paths are recorded and Q -> Z next
    # then every path would go from A to Z.
    @staticmethod
    def unchecked_union(sp_a: ShortestPaths, sp_b: ShortestPaths) -> ShortestPaths:
        shortest_path = ShortestPaths()
        for path_a in sp_a.paths:
            for path_b in sp_b.paths:
                shortest_path.paths.append(Path([*path_a, *path_b]))
        return shortest_path


# A Path Adjacency Matrix stores as a 2D Matrix 
# starting from every Node (rows) paths to every other Node (columns)
PathsAdjacencyMatrix = dict[str, dict[str, ShortestPaths]]
