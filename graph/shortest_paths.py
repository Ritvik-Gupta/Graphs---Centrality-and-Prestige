from __future__ import annotations


class Path(list[str]):
    def __repr__(self) -> str:
        return f"*{''.join(self)}"


class ShortestPaths:
    def __init__(self):
        self.paths: list[Path] = []

    def check_add(self, path: list[str]):
        if self.length() > len(path):
            self.paths = [Path(path)]
        elif self.length() == len(path):
            self.paths.append(Path(path))

    def unchecked_consume(self, other: ShortestPaths):
        for other_path in other.paths:
            if other_path not in self.paths:
                self.paths.append(other_path)

    def length(self, default_length=float("inf")) -> float:
        if len(self.paths) == 0:
            return default_length
        return len(self.paths[0])

    def __repr__(self) -> str:
        return repr(self.paths)

    @staticmethod
    def unchecked_union(sp_a: ShortestPaths, sp_b: ShortestPaths) -> ShortestPaths:
        shortest_path = ShortestPaths()
        for path_a in sp_a.paths:
            for path_b in sp_b.paths:
                shortest_path.paths.append(Path([*path_a, *path_b]))
        return shortest_path


PathsAdjacencyMatrix = dict[str, dict[str, ShortestPaths]]
